def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_1 = max(nums[66:94])
    nums.remove(max_1)
    if len(nums) < 2:
        return None
    max_2 = max(nums)
    return max_2