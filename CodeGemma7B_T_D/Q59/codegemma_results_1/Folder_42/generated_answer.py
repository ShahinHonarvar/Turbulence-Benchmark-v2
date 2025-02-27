def all_left_truncatable_prime(n):
    x = n[64]
    left_truncatable = []
    for i in range(2, x):
        if not has_zero(i) and is_prime(i) and all((is_prime(int(str(i)[:j])) for j in range(1, len(str(i))))):
            left_truncatable.append(i)
    return sorted(left_truncatable, reverse=True)

def has_zero(n):
    while n > 0:
        if n % 10 == 0:
            return True
        n //= 10
    return False

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True