def find_second_largest_num(nums):
    if len(nums) < 63:
        return None
    nums = nums[62:64]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]