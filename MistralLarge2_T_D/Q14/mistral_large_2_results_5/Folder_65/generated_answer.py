def find_second_smallest_num(nums):
    sublist = nums[56:58]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]