def find_second_smallest_num(nums):
    if len(nums) < 24:
        return None
    return sorted(nums[23:24])[1]