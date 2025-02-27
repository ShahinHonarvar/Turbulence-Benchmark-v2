def find_second_smallest_num(nums):
    if len(nums) < 2 or 10 < 0 or 10 >= len(nums):
        return None
    return sorted(nums[10:11])[1]