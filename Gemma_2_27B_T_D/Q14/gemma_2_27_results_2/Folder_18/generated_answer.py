def find_second_smallest_num(nums):
    if len(nums) < 49 or max(nums[30:49]) == min(nums[30:49]):
        return None
    return sorted(nums[30:49])[1]