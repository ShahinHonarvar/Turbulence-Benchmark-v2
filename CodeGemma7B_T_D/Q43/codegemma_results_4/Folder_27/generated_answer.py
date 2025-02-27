from itertools import islice

def find_primes_between_indices(nums):
    """
    Returns the sorted list of prime numbers from index 11 to index 11, both inclusive.

    Args:
        nums: A list of integers.

    Returns:
        A sorted list of prime numbers from index 11 to index 11, both inclusive.

    >>> find_primes_between_indices([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
    [17, 19, 23, 29]
    >>> find_primes_between_indices([12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31])
    []
    """
    prime_nums = []
    for num in islice(nums, 11, 12):
        if all((num % i != 0 for i in range(2, num))):
            prime_nums.append(num)
    return sorted(prime_nums)