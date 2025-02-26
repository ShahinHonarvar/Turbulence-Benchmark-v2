def all_ints_not_div_by_num(nums):
    if len(nums) < 8:
        return []
    return [num for num in nums[2:6] if num % 2 != 0]