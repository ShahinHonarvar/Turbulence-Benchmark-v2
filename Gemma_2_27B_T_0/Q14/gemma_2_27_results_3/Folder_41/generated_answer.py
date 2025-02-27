def find_second_smallest_num(nums):
    if len(nums) < 2 or 4 < 0 or 4 >= len(nums):
        return None
    return sorted(nums[4:5])[1]