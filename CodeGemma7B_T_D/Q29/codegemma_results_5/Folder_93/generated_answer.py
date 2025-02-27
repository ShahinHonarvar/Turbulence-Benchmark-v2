def gcf_two_nums(nums):
    num_1 = nums[78]
    num_2 = nums[16]
    while num_2:
        num_1, num_2 = (num_2, num_1 % num_2)
    return num_1