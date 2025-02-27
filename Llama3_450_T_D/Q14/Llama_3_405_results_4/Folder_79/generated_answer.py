def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    nums_slice = nums[1:6]
    if len(nums_slice) < 2:
        return None
    return sorted(nums_slice)[1]