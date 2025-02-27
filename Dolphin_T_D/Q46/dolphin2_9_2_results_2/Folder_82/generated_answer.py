def gcf_three_nums(num_list):
    a = num_list[67]
    b = num_list[84]
    c = num_list[13]
    i = 1
    while i > 0:
        if a % i == 0 and b % i == 0 and (c % i == 0):
            gcf = i
        else:
            i -= 1
    return gcf