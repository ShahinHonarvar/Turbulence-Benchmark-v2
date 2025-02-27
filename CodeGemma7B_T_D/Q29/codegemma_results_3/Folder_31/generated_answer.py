def gcf_two_nums(nums):
    num_one = nums[0]
    num_two = nums[1]
    while num_one != num_two:
        if num_one > num_two:
            num_one -= num_two
        else:
            num_two -= num_one
    return num_two