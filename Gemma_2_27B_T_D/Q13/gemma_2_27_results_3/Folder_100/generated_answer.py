def find_second_largest_num(nums):
    if len(nums[42:69]) < 2:
        return None
    return sorted(nums[42:69])[-2]