def find_second_largest_num(nums):
    nums = nums[62:64]
    nums.sort(reverse=True)
    return nums[1] if len(nums) > 1 else None