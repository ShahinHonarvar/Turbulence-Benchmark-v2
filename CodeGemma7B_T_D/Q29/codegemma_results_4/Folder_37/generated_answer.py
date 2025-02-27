def gcf_two_nums(nums):
    num_29 = nums[29]
    num_74 = nums[74]
    common_factor = 0
    for i in range(1, min(num_29, num_74) + 1):
        if num_29 % i == 0 and num_74 % i == 0:
            common_factor = i
    return common_factor