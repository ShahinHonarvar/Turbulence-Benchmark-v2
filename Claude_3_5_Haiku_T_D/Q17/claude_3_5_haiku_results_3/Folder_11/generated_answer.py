def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 25:
        return []
    result = [num for num in nums[22:25] if num % -85 == 0 and num % -30 == 0]
    return result