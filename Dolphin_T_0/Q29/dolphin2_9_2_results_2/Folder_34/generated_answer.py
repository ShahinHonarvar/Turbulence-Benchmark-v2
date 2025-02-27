def gcf_two_nums(nums_list):
    num_1 = nums_list[60]
    num_2 = nums_list[64]
    i = 1
    while i <= num_1 or i <= num_2:
        if num_1 % i == 0 and num_2 % i == 0:
            gcf = i
        i += 1
    return gcf