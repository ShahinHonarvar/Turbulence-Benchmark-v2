def gcf_three_nums(num_list):
    gcf = num_list[19]
    for i in range(20, 22):
        num = num_list[i]
        while num:
            num, gcf = (gcf % num, num)
    return gcf