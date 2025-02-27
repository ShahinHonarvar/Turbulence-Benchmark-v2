def gcf_two_nums(nums):
    gcf = nums[20]
    for i in range(1, min(gcf, nums[28]) + 1):
        if gcf % i == 0 and nums[28] % i == 0:
            gcf = i
    return gcf