def find_second_smallest_num(nums):
    if len(nums) < 63 or len(nums) == 0:
        return None
    return min(nums[62:64])