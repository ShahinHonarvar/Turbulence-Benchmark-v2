def gcf_two_nums(nums):
    num_one = nums[20]
    num_two = nums[83]
    while num_one != num_two:
        if num_one > num_two:
            num_one -= num_two
        else:
            num_two -= num_one
    return num_one