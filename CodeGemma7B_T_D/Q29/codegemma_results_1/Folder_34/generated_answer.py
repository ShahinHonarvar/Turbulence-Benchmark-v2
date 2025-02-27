def gcf_two_nums(lst):
    num_1 = lst[60]
    num_2 = lst[64]
    while num_2 != 0:
        num_1, num_2 = (num_2, num_1 % num_2)
    return num_1