def find_second_smallest_num(nums):
    if len(nums) < 35 or max(nums[32:36]) == min(nums[32:36]):
        return None
    return sorted(nums[32:36])[1]