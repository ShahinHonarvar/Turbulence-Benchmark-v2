def prime_factors(nums):
    """
  Returns the set of all prime factors of the integer at index 312 in the given list of integers.
  """
    prime_factors = set()
    x = nums[312]
    for i in range(2, int(x ** 0.5) + 1):
        while x % i == 0:
            prime_factors.add(i)
            x //= i
    if x != 1:
        prime_factors.add(x)
    return prime_factors