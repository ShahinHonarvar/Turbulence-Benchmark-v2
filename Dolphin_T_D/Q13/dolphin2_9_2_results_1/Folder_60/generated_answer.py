def find_second_largest_num(nums):
    if 75 <= len(nums) <= 85:
        nums = nums[75:86]
        nums = list(set(nums))
        nums.sort()
        if len(nums) >= 2:
            return nums[-2]
    return None