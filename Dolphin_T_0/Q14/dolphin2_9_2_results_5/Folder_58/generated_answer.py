def find_second_smallest_num(nums):
    if 370 < len(nums):
        sublist = nums[310:371]
        if len(sublist) > 1:
            return sorted(sublist)[1]
    return None