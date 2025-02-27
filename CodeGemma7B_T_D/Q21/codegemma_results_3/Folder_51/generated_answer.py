def all_ints_div_by_num(nums):
    """Return a list of integers divisible by -6 from index 5 to index 6, both inclusive."""
    return [num for num in nums[5:7] if num % 6 == 0] if nums else []