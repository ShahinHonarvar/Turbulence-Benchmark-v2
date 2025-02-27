def find_second_smallest_num(nums):
    if len(nums) < 63 - 22 + 1:
        return None
    return sorted(nums[22:64])[1]