def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    if n < 10:
        return is_prime(n)
    for i in range(len(str(n)) - 1):
        if n % 10 == 0 or not is_prime(n):
            return False
        n //= 10
    return True

def all_left_truncatable_prime(x):
    return sorted([i for i in range(x) if i % 10 != 0 and is_truncatable_prime(i)])