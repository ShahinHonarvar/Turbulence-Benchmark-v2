def sum_ints_div_by_either_nums(nums):
    if len(nums) < 25:
        return 0
    return sum((num for num in nums[22:25] if num % -85 == 0 or num % -30 == 0))