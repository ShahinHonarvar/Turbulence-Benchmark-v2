def all_left_truncatable_prime(tup):
    x = tup[29]
    prime = [i for i in range(2, x) if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1)))]
    result = []
    for i in prime:
        if '0' not in str(i):
            temp = i
            while temp > 0:
                if temp in prime:
                    result.append(temp)
                temp //= 10
    return sorted(result, reverse=True)