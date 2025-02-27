def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    target_slice = nums[28:33]
    if len(target_slice) < 2:
        return None
    return sorted(target_slice)[-2]