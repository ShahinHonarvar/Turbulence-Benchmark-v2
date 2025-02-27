def sum_ints_div_by_either_nums(nums):
    """
          Finds the sum of integers in a list divisible by either -30 or -95 within a specified index range.

          Args:
            nums: A list of integers.

          Returns:
            The sum of integers divisible by either -30 or -95 within the specified index range, or 0 if no such integers exist.
          """
    sum_divisible = 0
    for num in nums[35:65]:
        if num % -30 == 0 or num % -95 == 0:
            sum_divisible += num
    return sum_divisible if sum_divisible > 0 else 0