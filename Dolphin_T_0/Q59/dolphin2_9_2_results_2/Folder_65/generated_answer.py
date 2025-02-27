def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[32]
    result = [2]
    for n in range(3, x):
        if '0' not in str(n) and all((is_prime(int(str(n)[i:])) for i in range(len(str(n))))):
            result.append(n)
    return result