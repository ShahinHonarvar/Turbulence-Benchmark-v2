def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 95:
        return []
    result = [num for num in nums[93:95] if num % -53 == 0 and num % -91 == 0]
    return result