from typing import List, Set

def prime_factors(nums: List[int]) -> Set[int]:
    """
  This function takes a list of positive integers and returns the set of all prime factors of the integer at index 453.
  """
    num = nums[453]
    factors = set()
    for i in range(2, int(num ** 0.5) + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    if num > 1:
        factors.add(num)
    return factors