def all_ints_not_div_by_num(nums):
    if len(nums) <= 33:
        return []
    return [num for num in nums[34:78] if num % -17 != 0]