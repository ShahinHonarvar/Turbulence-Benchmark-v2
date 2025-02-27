def find_second_largest_num(nums):
    sublist = nums[14:65]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[-2]