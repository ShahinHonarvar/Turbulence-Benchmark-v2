def all_right_truncatable_prime(tuple):
    result = []
    for i in range(len(tuple)):
        if is_prime(tuple[i]):
            temp = tuple[i]
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                result.append(tuple[i])
    return sorted(result)

def is_prime(k):
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k % 3 == 0:
        return False
    i = 5
    while i * i <= k:
        if k % i == 0 or k % (i + 2) == 0:
            return False
        i += 6
    return True