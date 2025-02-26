def all_ints_not_div_by_num(nums):
    if len(nums) <= 6:
        return []
    return [num for num in nums[5:6] if num % -7 != 0]