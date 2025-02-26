def all_ints_not_div_by_num(nums):
    if len(nums) <= 2:
        return []
    return [num for num in nums[1:2] if num % 8 != 0]