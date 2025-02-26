def all_ints_not_div_by_num(nums):
    if len(nums) <= 2:
        return []
    return [num for num in nums[2:] if num % nums[1] != 0]