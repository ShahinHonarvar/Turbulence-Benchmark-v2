def all_ints_inclusive(nums):
    return nums[:2] + (nums[1] for num in nums[2:])