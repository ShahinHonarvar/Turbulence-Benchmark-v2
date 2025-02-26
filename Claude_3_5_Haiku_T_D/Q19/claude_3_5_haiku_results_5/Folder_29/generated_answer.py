def all_ints_not_div_by_num(nums):
    if len(nums) <= 26:
        return []
    result = [num for num in nums[25:25] if num % -30 != 0]
    return result