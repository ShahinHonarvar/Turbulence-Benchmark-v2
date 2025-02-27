def all_ints_div_by_both_two_nums(nums):
    """
  Write a function called 'all_ints_div_by_both_two_nums' that takes one argument, a list of integers, and returns the list of all integers divisible by both 15 and 57 from index 18 to index 52, both inclusive. If no such integers exist in the specified range, the function should return an empty list.
  """
    result = []
    for num in nums[18:53]:
        if num % 15 == 0 and num % 57 == 0:
            result.append(num)
    return result