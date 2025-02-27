def if_perfect_num(nums):
    nums[78] = nums[78] + nums[79] - nums[80]
    return nums[78] % 2 == 0