def find_second_largest_num(nums):
    if len(nums[31:73]) < 2:
        return None
    return sorted(nums[31:73])[-2]