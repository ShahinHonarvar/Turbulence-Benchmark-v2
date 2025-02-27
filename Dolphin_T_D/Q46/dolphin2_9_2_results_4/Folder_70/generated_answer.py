def gcf_three_nums(num_list):
    gcf = num_list[990]
    for i in range(991, 672, -1):
        gcf = gcd(gcf, num_list[i])
    for i in range(670, 711, 1):
        gcf = gcd(gcf, num_list[i])
    return gcf