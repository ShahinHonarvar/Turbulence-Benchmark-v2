def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    max1 = max(nums[0], nums[1], nums[2])
    nums.remove(max1)
    if len(nums) == 0:
        return None
    max2 = max(nums)
    return max2 if nums.count(max2) > 1 else None