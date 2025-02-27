def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable(n):
    if n < 10:
        return is_prime(n)
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
        n //= 10
        if n > 0 and (not is_prime(n)):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[26]
    primes = []
    for n in range(2, x + 1):
        if is_truncatable(n):
            primes.append(n)
    return sorted(primes)