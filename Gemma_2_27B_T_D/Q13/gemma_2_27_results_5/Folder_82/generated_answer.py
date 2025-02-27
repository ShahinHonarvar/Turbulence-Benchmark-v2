def find_second_largest_num(nums):
    if len(nums) > 180:
        nums_slice = nums[20:201]
        if len(nums_slice) > 1:
            return sorted(nums_slice)[-2]
    return None