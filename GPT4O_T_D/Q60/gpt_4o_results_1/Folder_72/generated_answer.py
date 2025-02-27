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

def is_left_right_truncatable(prime):
    str_prime = str(prime)
    if '0' in str_prime:
        return False
    for i in range(1, len(str_prime)):
        if not (is_prime(int(str_prime[i:])) and is_prime(int(str_prime[:-i]))):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 31:
        return []
    x = numbers[31]
    primes = [n for n in range(11, x + 1) if is_prime(n)]
    left_right_truncatable_primes = [p for p in primes if is_left_right_truncatable(p)]
    return sorted(left_right_truncatable_primes, reverse=True)