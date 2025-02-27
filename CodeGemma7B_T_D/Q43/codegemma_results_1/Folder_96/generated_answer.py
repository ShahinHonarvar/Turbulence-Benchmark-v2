def find_primes_between_indices(nums):
    """
  Finds all prime numbers between two indices, inclusive.

  Args:
    nums: A list of integers.

  Returns:
    A sorted list of prime numbers between the specified indices, in descending order.
    If no prime number exists in the specified range, an empty list is returned.
  """
    if len(nums) < 68 or len(nums) <= 31:
        return []
    primes = []
    for i in range(31, 68):
        is_prime = True
        for j in range(5, i, 6):
            if i % j == 0 or i % (j + 2) == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nums[i])
    primes.sort(reverse=True)
    return primes