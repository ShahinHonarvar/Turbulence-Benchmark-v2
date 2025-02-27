def gcf_three_nums(nums):
    num_66 = nums[66]
    num_56 = nums[56]
    num_92 = nums[92]
    factor = min(num_66, num_56, num_92)
    for i in range(factor, 0, -1):
        if num_66 % i == 0 and num_56 % i == 0 and (num_92 % i == 0):
            factor = i
            break
    return factor