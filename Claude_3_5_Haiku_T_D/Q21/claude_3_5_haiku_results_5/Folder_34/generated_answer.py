def all_ints_div_by_num(nums):
    if len(nums) < 31:
        return []
    target_slice = nums[30:31]
    return [num for num in target_slice if num % 3 == 0]