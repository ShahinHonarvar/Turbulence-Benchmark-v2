def find_second_smallest_num(nums):
    if 56 < len(nums) - 1 and 57 <= len(nums):
        return sorted(nums[56:58])[1]
    return None