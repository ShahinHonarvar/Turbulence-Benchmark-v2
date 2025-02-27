def find_second_largest_num(nums):
    if len(nums) < 3 or nums[4] == nums[8]:
        return None
    max1 = max(nums[4:9])
    nums.remove(max1)
    if len(nums) < 2 or max1 == nums[4]:
        return None
    max2 = max(nums[4:9])
    return max2