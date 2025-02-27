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

def right_truncatable_primes(n):
    if n < 10:
        return [n] if is_prime(n) else []
    result = []
    for i in range(10):
        if n % 10 != i:
            continue
        candidate = int(str(n)[:-1])
        if candidate and is_prime(candidate):
            result.extend(right_truncatable_primes(candidate))
    return result

def all_right_truncatable_prime(numbers):
    x = numbers[630]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            primes.extend(right_truncatable_primes(num))
    return sorted(primes, reverse=True)