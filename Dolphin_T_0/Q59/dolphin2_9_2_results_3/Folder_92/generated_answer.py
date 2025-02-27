def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_left_truncatable_prime(n):
    while n:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(x):
    return [i for i in range(2, x) if is_left_truncatable_prime(i) and i % 10 != 0]