def gcf_two_nums(num_list):
    x = num_list[96]
    y = num_list[57]
    while y:
        x, y = (y, x % y)
    return x