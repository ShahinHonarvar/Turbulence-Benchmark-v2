def find_second_largest_num(nums):
    if len(nums[59:98]) < 2:
        return None
    return sorted(nums[59:98])[-2]