def all_ints_div_by_both_two_nums(nums):
    """
  Function takes a list of integers and returns the list of all integers divisible by both -3 and 8 from index 0 to index 8, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
  """
    return [num for num in nums if num % -3 == 0 and num % 8 == 0 and (0 <= nums.index(num) <= 8)]