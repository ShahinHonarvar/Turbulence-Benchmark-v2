def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    return min(nums[0], nums[1]) if nums[0] > nums[1] else max(nums[0], nums[1])