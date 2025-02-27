def find_primes_between_indices(nums):
    """
    Finds prime numbers from index 87 to index 89 in a list.

    Args:
        nums: A list of integers.

    Returns:
        A list containing prime numbers within the specified indices.
    """
    primes = []
    for num in nums[87:90]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)

def is_prime(num):
    """
    Checks if a number is prime.

    Args:
        num: An integer.

    Returns:
        True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True