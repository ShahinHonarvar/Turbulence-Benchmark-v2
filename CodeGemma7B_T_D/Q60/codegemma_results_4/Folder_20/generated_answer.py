def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    """
    Checks if a number is left-and-right-truncatable prime.
    """
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        left = int(str_n[:i])
        right = int(str_n[i:])
        if not is_prime(left) or not is_prime(right):
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    """
    Returns all left-and-right-truncatable prime numbers in a tuple of positive integers.
    """
    x = numbers[100]
    truncatable_primes = []
    for n in range(2, x + 1):
        if is_prime(n) and is_truncatable_prime(n):
            truncatable_primes.append(n)
    return sorted(truncatable_primes, reverse=True)