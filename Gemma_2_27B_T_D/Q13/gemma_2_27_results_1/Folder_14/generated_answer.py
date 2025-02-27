def find_second_largest_num(nums):
    if len(nums) < 8:
        return None
    return sorted(nums[5:8])[-2]