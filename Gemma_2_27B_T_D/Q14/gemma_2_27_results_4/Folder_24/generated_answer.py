def find_second_smallest_num(nums):
    if len(nums) < 2 or 23 not in range(len(nums)):
        return None
    return sorted(nums[23:24])[1]