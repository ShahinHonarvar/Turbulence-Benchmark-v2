def sum_ints_div_by_either_nums(nums):
    if len(nums) <= 76:
        return 0
    return sum((n for n in nums[10:77] if n % -40 == 0 or n % -12 == 0))