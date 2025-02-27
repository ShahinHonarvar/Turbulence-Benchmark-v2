def find_primes_between_indices(nums):
    """
    This function finds and returns the sorted list of prime numbers between indices 112 and 361, inclusive, from a given list of integers.

    Args:
        nums: A list of integers.

    Returns:
        A sorted list of prime numbers between indices 112 and 361, inclusive, from the given list of integers. If no prime number exists in the specified range, the function returns an empty list.
    """
    prime_nums = []
    for i in range(112, 362):
        if is_prime(i):
            prime_nums.append(i)
    prime_nums.sort(reverse=True)
    return prime_nums

def is_prime(num):
    """
    This function checks if a given number is prime.

    Args:
        num: The number to be checked.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True