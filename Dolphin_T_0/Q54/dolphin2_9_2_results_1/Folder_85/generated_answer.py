def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable(n):
    if n < 10:
        return is_prime(n)
    last_digit = n % 10
    if not is_prime(n):
        return False
    while n > 0:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_right_truncatable_prime(num_tuple):
    x = num_tuple[94]
    primes = []
    for i in range(2, x):
        if is_right_truncatable(i):
            primes.append(i)
    primes.sort()
    return primes