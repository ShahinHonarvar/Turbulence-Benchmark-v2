def sum_ints_div_by_either_nums(nums):
    if len(nums) < 25:
        return 0
    target_slice = nums[22:25]
    divisible_nums = [num for num in target_slice if num % -85 == 0 or num % -30 == 0]
    return sum(divisible_nums)