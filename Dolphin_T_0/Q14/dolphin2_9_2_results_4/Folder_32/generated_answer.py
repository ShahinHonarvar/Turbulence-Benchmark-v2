def find_second_smallest_num(nums):
    if 32 <= len(nums) < 36:
        nums = nums[32:36]
        nums.sort()
        if len(nums) >= 2:
            return nums[1]
    return None