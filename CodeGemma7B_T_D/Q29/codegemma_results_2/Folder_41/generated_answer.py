def gcf_two_nums(some_list):
    big = max(some_list[23], some_list[27])
    small = min(some_list[23], some_list[27])
    while big % small != 0:
        big, small = (big % small, big)
    return small