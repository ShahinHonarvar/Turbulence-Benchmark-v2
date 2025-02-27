def all_right_truncatable_prime(numbers):
    x = numbers[98]
    primes = set()
    for i in range(2, x):
        for x in range(numbers[98], 1, -1):
            if is_prime(x) and is_right_truncatable(x):
                primes.add(x)
    return sorted(list(primes))

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

def is_right_truncatable(n):
    while n > 0:
        if not is_prime(n):
            return False
        n = int(n / 10)
    return True