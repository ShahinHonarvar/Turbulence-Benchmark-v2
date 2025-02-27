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

def is_left_truncatable(n):
    if n < 10:
        return is_prime(n)
    return is_left_truncatable(int(str(n)[1:])) and is_prime(n)

def all_left_truncatable_prime(x):
    primes = []
    digits = len(str(x))
    for num in range(1, 10):
        if is_left_truncatable(num):
            primes.append(num)
    for num in range(10, x):
        if is_left_truncatable(num):
            primes.append(num)
    return sorted(primes)