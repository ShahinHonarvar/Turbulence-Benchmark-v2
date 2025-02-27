def find_second_smallest_num(nums):
    nums_sliced = nums[3:6]
    if len(nums_sliced) < 2:
        return None
    return sorted(nums_sliced)[1]