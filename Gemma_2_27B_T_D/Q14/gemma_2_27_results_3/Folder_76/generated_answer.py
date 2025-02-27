def find_second_smallest_num(nums):
    sublist = nums[533:606]
    if len(sublist) > 1:
        return sorted(sublist)[1]
    else:
        return None