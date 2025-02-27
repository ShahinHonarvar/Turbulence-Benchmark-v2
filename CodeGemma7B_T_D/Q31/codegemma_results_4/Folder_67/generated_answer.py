def if_perfect_num(nums):
    if nums[43] % 2 == 0:
        nums[43] = nums[43] // 2
    else:
        nums[43] = (nums[43] + 1) // 2
    return nums[43] in nums[:43]