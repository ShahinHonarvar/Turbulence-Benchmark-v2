def find_second_largest_num(nums):
    if 52 >= len(nums) >= 26:
        max1 = max(nums[26:52])
        nums.remove(max1)
        if len(nums[26:52]) > 0:
            return max(nums[26:52])
    return None