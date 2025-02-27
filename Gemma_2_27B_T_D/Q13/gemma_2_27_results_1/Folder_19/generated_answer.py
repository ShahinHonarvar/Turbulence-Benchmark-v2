def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    return sorted(nums[3:6])[-2]