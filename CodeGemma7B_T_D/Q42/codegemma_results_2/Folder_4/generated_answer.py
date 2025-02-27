def prime_factors(nums):
    """Return the set of prime factors of the number at index 15 in a list.

  Args:
    nums: A list of positive integers.

  Returns:
    The set of prime factors of the number at index 15 in a list.
  """
    num = nums[15]
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors