def gcf_two_nums(nums):
    num_1 = nums[380]
    num_2 = nums[327]
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 -= num_2
        else:
            num_2 -= num_1
    return num_1