def sum_odd_ints_inclusive(nums):
    """
    Sums all odd integers from index 6 to index 8, inclusive.

    Args:
      nums: A list of integers.

    Returns:
      The sum of all odd integers from index 6 to index 8, inclusive. If no odd integers exist in the specified range, the function should return 0.
    """
    has_odd_nums = False
    for num in nums[6:9]:
        if num % 2 != 0:
            has_odd_nums = True
    if not has_odd_nums:
        return 0
    sum_odd_nums = 0
    for num in nums[6:9]:
        if num % 2 != 0:
            sum_odd_nums += num
    return sum_odd_nums