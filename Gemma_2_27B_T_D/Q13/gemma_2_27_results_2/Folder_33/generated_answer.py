def find_second_largest_num(nums):
    if len(nums[667:775]) < 2:
        return None
    return sorted(nums[667:775])[-2]