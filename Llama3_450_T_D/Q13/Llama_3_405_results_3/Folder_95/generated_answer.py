def find_second_largest_num(nums):
    if len(nums[82:87]) < 2:
        return None
    else:
        return sorted(nums[82:87], reverse=True)[1]