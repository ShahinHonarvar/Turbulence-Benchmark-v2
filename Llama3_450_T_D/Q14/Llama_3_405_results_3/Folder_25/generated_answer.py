def find_second_smallest_num(nums):
    specific_range = nums[37:77]
    if len(specific_range) < 2:
        return None
    specific_range.sort()
    return specific_range[1]