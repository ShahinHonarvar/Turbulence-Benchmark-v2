def find_second_smallest_num(nums):
    if len(nums) < 57 or 56 not in range(len(nums)):
        return None
    return sorted(nums[56:58])[1]