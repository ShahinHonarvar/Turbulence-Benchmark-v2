def gcf_two_nums(num_list):
    x, y = (num_list[28], num_list[49])
    r = x % y
    while r != 0:
        x, y = (y, r)
        r = x % y
    return y