def find_second_smallest_num(nums):
    nums = nums[52:72]
    nums.sort()
    return nums[1] if len(nums) >= 2 else None