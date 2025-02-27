def all_right_truncatable_prime(num):
    prime = num[645]
    result = []
    for x in range(prime):
        factor = 2
        result.append(x)
        result.append(-x)
        while factor <= x:
            if x % factor == 0:
                result.remove(x)
                result.remove(-x)
                break
            factor += 1
    return sorted(list(set(result)))