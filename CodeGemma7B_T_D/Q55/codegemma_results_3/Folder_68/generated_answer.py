from itertools import combinations

def lists_with_product_equal_n(nums):
    """Return a list of sublists each of which contains contiguous integers from the list
  that have a product equal to 6, in any order.  The sublists can be of any size
  as long as they are smaller than the list.  Note that the list is circular.

  Args:
    nums: A circular list of integers.

  Returns:
    A list of sublists each of which has elements with product equal to 6, in any order.
  """
    seen = set()
    prod = 1
    results = []
    for i, num in enumerate(nums):
        prod *= num
        for j in range(i - len(nums) + 1, i + 1):
            g = nums[j % len(nums)]
            if prod // g in seen:
                results.append([num for num in nums[j:i + 1]])
            seen.add(prod)
    return results