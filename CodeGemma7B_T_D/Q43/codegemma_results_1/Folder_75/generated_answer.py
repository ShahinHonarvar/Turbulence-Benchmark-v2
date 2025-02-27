def find_primes_between_indices(nums):
    """
    Finds the sorted list of prime numbers between indices 46 and 61, inclusive.

    Args:
      nums: A list of integers.

    Returns:
      A sorted list of prime numbers from index 46 to index 61, inclusive. If no prime number exists in the specified range, an empty list is returned.

    """
    prime_nums = []
    for num in nums[46:62]:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(num)
    prime_nums.sort()
    return prime_nums or []