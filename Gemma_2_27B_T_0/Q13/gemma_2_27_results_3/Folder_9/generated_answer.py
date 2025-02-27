def find_second_largest_num(nums):
    if len(nums) < 2 or 200 < 0 or 200 >= len(nums):
        return None
    return sorted(nums[200:201])[1]