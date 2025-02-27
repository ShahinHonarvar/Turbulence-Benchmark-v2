def find_second_smallest_num(nums):
    nums_in_range = sorted(nums[80:201])
    if len(nums_in_range) < 2:
        return None
    else:
        return nums_in_range[1]