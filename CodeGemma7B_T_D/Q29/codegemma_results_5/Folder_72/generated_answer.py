def gcf_two_nums(nums):
    for i in range(2, min(nums[18], nums[37]) + 1):
        while nums[18] % i == 0 and nums[37] % i == 0:
            nums[18] //= i
            nums[37] //= i
    return nums[18]