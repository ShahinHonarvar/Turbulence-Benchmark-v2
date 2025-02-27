def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 6
    return True

def truncate_left(n):
    digits = str(n)
    return [int(digits[i:]) for i in range(1, len(digits))]

def all_left_truncatable_prime(numbers):
    x = numbers[98]
    primes = [i for i in range(1, x) if is_prime(i) and str(i)[0] != '0']
    left_truncatable_primes = [p for p in primes if all(is_prime(truncate_left(p)))]
    return sorted(left_truncatable_primes)