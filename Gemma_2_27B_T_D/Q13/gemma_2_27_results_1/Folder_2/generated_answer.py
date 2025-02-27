def find_second_largest_num(nums):
    if len(nums[15:40]) < 2:
        return None
    return sorted(nums[15:40])[-2]