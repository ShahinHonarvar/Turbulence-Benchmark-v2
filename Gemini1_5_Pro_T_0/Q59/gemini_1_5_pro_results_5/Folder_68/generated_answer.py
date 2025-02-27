def is_prime(n):
    """Primality test using 6k ± 1 optimization."""
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
    if n < 10 or not is_prime(n):
        return False
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
    return True

def all_left_truncatable_prime(numbers):
    """
    Find all left-truncatable prime numbers less than x,
    where x is the integer at index 1 of the input tuple.
    """
    x = numbers[1]
    left_truncatable_primes = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            left_truncatable_primes.append(i)
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes