def find_second_largest_num(nums):
    if len(nums[82:87]) < 2:
        return None
    return sorted(nums[82:87])[-2]