def find_second_smallest_num(nums):
    nums_in_range = sorted(nums[262:747])
    if len(nums_in_range) < 2:
        return None
    return nums_in_range[1]