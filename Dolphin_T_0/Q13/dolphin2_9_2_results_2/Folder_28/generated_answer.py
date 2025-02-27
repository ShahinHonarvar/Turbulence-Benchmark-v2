def find_second_largest_num(nums):
    if 62 <= len(nums) <= 63:
        nums = nums[62:64]
        nums.sort()
        if len(nums) == 2:
            return nums[1]
    return None