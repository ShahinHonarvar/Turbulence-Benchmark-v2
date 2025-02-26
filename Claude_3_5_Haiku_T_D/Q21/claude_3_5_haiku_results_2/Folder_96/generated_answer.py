def all_ints_div_by_num(nums):
    if len(nums) <= 20:
        return []
    target_range = nums[20:21]
    return [num for num in target_range if num % 2 == 0]