def find_second_largest_num(nums):
    if 5 < len(nums) - 1 and 7 < len(nums):
        return sorted(nums[5:8])[-2]
    return None