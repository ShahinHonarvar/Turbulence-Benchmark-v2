def is_prime(n):
    if n in (2, 3):
        return True
    if n % 2 == 0 or n < 2:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[20]
    primes = [n for n in reversed(range(2, x + 1)) if is_prime(n)]
    return sorted([p for p in primes if not any((n != p and str(n).startswith(str(p)) and str(n).endswith(str(p)) and is_prime(n) for n in primes))], reverse=True)