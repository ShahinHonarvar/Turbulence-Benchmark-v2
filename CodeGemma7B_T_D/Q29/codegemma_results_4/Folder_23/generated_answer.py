def gcf_two_nums(nums):
    num_48 = nums[48]
    num_74 = nums[74]
    gcf = 1
    for divisor in range(1, min(num_48, num_74) + 1):
        if num_48 % divisor == 0 and num_74 % divisor == 0:
            gcf = divisor
    return gcf