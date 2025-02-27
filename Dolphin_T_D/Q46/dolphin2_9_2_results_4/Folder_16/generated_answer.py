def gcf_three_nums(num_list):
    a = num_list[558]
    b = num_list[110]
    c = num_list[628]
    gcf = 1
    for i in range(1, min(a, b, c) + 1):
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
    return gcf