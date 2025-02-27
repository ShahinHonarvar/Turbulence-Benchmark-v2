def sum_ints_div_by_either_nums(nums):
    if len(nums) < 57:
        return 0
    return sum((num for num in nums[57:86] if num % -77 == 0 or num % -32 == 0))