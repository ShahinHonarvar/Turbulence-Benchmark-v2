def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    return min(nums[0:2])