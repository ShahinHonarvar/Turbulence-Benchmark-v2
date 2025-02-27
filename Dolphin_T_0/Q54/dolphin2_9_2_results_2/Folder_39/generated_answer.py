def is_prime(n):
    if n in (0, 1):
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    m = int(n ** 0.5) + 1
    for x in range(3, m, 2):
        if n % x == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    if is_prime(n):
        while n != 0:
            n = n // 10
            if not is_prime(n):
                return False
        return True
    return False

def all_right_truncatable_prime(numbers):
    x = numbers[30]
    primes = [i for i in range(x, 1, -1) if is_right_truncatable_prime(i)]
    return primes if primes else []