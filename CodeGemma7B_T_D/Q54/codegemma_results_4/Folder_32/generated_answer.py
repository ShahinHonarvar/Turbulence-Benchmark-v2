from math import sqrt

def right_truncatable_prime(n):
    """Return sorted list of right-truncatable prime numbers less than n."""
    result = []
    for i in range(2, n):
        if is_prime(i):
            j = i % 10
            while j != 0:
                if not is_prime(i // j):
                    break
                j = i // j // 10
            else:
                result.append(i)
    return sorted(result)

def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True