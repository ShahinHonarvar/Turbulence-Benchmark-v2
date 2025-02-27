def prime(n):
    """Determines if n is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    """Determines if n is a left-truncatable prime."""
    if '0' in str(n):
        return False
    while n >= 2:
        if not prime(n):
            return False
        n //= 10
    return True

def right_truncatable_prime(n):
    """Determines if n is a right-truncatable prime."""
    if '0' in str(n):
        return False
    for i in range(len(str(n))):
        if not prime(int(str(n)[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(nums):
    """Returns all left-and-right-truncatable prime numbers less than or equal to x."""
    x = nums[29]
    result = []
    for n in range(limit):
        if prime(n) and left_truncatable_prime(n) and right_truncatable_prime(n):
            result.append(n)
    return result[::-1]