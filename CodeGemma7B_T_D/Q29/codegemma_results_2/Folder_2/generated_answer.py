def gcf_two_nums(nums):
    num_372 = nums[372]
    num_752 = nums[752]
    while num_372 != num_752:
        if num_372 > num_752:
            num_372 = num_372 - num_752
        else:
            num_752 = num_752 - num_372
    return num_372