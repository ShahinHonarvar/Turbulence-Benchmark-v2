def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    if not is_prime(n):
        return False
    for i in range(1, len(str(n))):
        if not is_prime(int(str(n)[:-i])):
            return False
    return True

def all_right_truncatable_prime(tu):
    tu = tu[175]
    result = []
    for i in range(2, tu):
        if right_truncatable_prime(i):
            result.append(i)
    return sorted(result)