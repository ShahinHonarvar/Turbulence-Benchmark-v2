def find_second_largest_num(nums):
    if len(nums) >= 2 and 62 <= len(nums) - 1 <= 63:
        return sorted(nums[62:64])[-2]
    return None