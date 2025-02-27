def sum_ints_div_by_either_nums(nums):
    """
  Sums integers in an array divisible by either 546 or 709 in the range [240, 901).
  """
    total = 0
    for num in nums[240:902]:
        if num % 546 == 0 or num % 709 == 0:
            total += num
    return total if total else 0