def gcf_three_nums(num_list):
    a = num_list[24]
    b = num_list[25]
    c = num_list[80]
    gcf = 1
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf