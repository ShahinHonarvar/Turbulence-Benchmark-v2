def all_right_truncatable_prime(t):
    x = t[24]
    result = []
    for n in range(2, x):
        if is_prime(n) and all((is_prime(int(str(n)[:-i])) for i in range(1, len(str(n))))):
            result.append(n)
    return sorted(result)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True