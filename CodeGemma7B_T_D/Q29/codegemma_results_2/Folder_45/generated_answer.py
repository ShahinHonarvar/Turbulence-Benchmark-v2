def gcf_two_nums(nums):
    num_47 = nums[47]
    num_97 = nums[97]
    while num_47 != num_97:
        if num_47 > num_97:
            num_47 = num_47 - num_97
        else:
            num_97 = num_97 - num_47
    return num_47