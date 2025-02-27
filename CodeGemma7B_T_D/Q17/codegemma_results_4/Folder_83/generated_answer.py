def all_ints_div_by_both_two_nums(nums):
    """
  This function takes one argument, a list of integers, and returns the list of all integers divisible by both -31 and 13 from index 90 to index 200, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for num in nums[90:201]:
        if num % 31 == 0 and num % 13 == 0:
            result.append(num)
    return result