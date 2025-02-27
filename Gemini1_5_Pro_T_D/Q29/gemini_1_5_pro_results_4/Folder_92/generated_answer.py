def gcf_two_nums(nums):
    i = 1
    gcf = 1
    while i <= nums[0] and i <= nums[1]:
        if nums[0] % i == 0 and nums[1] % i == 0:
            gcf = i
        i += 1
    return gcf