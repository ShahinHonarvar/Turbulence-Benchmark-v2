def sum_ints_div_by_either_nums(nums):
    if len(nums) < 95:
        return 0
    return sum([num for num in nums[93:95] if num % -53 == 0 or num % -91 == 0])