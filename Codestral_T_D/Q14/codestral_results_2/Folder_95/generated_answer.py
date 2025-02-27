def find_second_smallest_num(nums):
    nums_in_range = sorted(nums[75:86])
    if len(nums_in_range) >= 2:
        return nums_in_range[1]
    return None