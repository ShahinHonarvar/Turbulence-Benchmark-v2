def is_prime(n):
    """Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_left_truncatable_prime(n):
    """Check if a number is a left-truncatable prime."""
    if not is_prime(n):
        return False
    if n < 10:
        return True
    if '0' in str(n):
        return False
    return is_left_truncatable_prime(int(str(n)[1:]))

def all_left_truncatable_prime(numbers):
    """Find all left-truncatable primes less than the number at index 64."""
    x = numbers[64]
    left_truncatable_primes = []
    for num in range(2, x):
        if is_left_truncatable_prime(num):
            left_truncatable_primes.append(num)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes