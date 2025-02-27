def find_second_smallest_num(nums):
    if len(nums) < 32:
        return None
    return sorted(nums[28:33])[1]