def gcf_three_nums(nums):
    num_1 = nums[2]
    num_2 = nums[5]
    num_3 = nums[8]
    if num_1 > num_2:
        num_great = num_1
    else:
        num_great = num_2
    for i in range(1, num_great + 1):
        if num_1 % i == 0 and num_2 % i == 0 and (num_3 % i == 0):
            gcf = i
    return gcf