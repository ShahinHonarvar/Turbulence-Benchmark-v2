def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncatables(prime):
    while prime > 0:
        if not is_prime(prime):
            return False
        prime //= 10
    return True

def all_right_truncatable_prime(numbers):
    x = numbers[43]
    truncatable_primes = []
    for num in range(2, x):
        if right_truncatables(num):
            truncatable_primes.append(num)
    truncatable_primes.sort()
    return truncatable_primes