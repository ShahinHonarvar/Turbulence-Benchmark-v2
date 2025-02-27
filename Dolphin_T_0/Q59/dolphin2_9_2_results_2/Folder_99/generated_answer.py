def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[758]
    result = []
    for n in range(2, x):
        trunc = n
        while trunc:
            if is_prime(trunc):
                trunc //= 10
            else:
                break
        else:
            result.append(n)
    return sorted(result)