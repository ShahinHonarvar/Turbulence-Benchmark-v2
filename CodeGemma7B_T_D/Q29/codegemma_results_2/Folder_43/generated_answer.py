def gcf_two_nums(num_list):
    gcf = num_list[59]
    for i in range(59, 94):
        gcf = denominator(gcf, num_list[i])
    return gcf