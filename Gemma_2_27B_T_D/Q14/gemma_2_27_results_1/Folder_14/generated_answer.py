def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    return min(nums[8:10])