def all_ints_div_by_num(nums):
    if len(nums) < 11:
        return []
    return [num for num in nums[10:11] if num % 1 == 0]