def gcf_three_nums(num_list):
    gcf = num_list[0]
    for i in range(1, min(len(num_list), 8)):
        gcf = gcd(gcf, num_list[i])
    return gcf