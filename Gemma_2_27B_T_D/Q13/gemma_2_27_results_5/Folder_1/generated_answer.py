def find_second_largest_num(nums):
    if 31 < len(nums) <= 72:
        return sorted(nums[31:73])[-2]
    return None