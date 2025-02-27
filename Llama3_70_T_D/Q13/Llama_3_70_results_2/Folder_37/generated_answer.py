def find_second_largest_num(nums):
    if len(nums[1:6]) < 2:
        return None
    else:
        return sorted(nums[1:6])[-2]