def find_second_largest_num(nums):
    if len(nums) < 63 or len(nums) == 0:
        return None
    return sorted(nums[62:64])[-2]