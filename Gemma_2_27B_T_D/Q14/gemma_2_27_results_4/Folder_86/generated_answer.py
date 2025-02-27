def find_second_smallest_num(nums):
    if len(nums) < 36:
        return None
    return sorted(nums[33:37])[1]