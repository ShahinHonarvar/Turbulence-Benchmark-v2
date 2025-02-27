def gcf_two_nums(nums):
    gcf = nums[30]
    for i in range(1, min(nums[37], nums[30]) + 1):
        if nums[37] % i == 0 and nums[30] % i == 0:
            gcf = i
    return gcf