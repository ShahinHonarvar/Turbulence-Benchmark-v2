def gcf_two_nums(nums):
    num_1 = nums[15]
    num_2 = nums[99]
    greater_num = max(num_1, num_2)
    while num_2 != 0:
        temp = num_2
        num_2 = num_1 % num_2
        num_1 = temp
    return num_1