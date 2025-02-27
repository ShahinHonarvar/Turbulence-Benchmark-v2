def find_second_largest_num(nums):
    if len(nums[3:6]) < 2:
        return None
    else:
        return sorted(nums[3:6])[1]