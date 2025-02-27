def gcf_three_nums(nums):
    return nums[21] // gcf(nums[21], nums[69], nums[41]) * nums[69] // gcf(nums[21], nums[69], nums[41]) * nums[41] // gcf(nums[21], nums[69], nums[41])