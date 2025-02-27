def find_second_smallest_num(nums):
    sublist = nums[74:96]
    if not sublist:
        return None
    return sorted(sublist)[1]