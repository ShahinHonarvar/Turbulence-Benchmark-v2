def find_second_largest_num(nums):
    if len(nums) < 2 or 90 >= len(nums) or 90 < 0:
        return None
    return sorted(nums[90:91 + 1])[-2]