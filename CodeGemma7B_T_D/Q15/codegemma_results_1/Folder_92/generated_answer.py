def sum_odd_ints_inclusive(nums):
    """
  This function takes one argument, a list of integers,
  and returns the sum of all odd integers from index 1 to index 1,
  both inclusive. If no odd integers exist in the specified range,
  the function should return 0.
  """
    sum_odd = 0
    for num in nums:
        if num % 2 != 0:
            sum_odd += num
    return sum_odd