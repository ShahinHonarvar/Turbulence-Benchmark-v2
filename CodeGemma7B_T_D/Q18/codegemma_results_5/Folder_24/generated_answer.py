def sum_ints_div_by_either_nums(nums):
    """Sums integers divisible by either -68 or -85 from index 29 to 53 inclusive."""
    result = 0
    for num in nums[29:54]:
        if num % -68 == 0 or num % -85 == 0:
            result += num
    return result if result else 0