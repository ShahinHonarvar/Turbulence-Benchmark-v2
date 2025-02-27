def gcf_two_nums(lst):
    num_1 = lst[56]
    num_2 = lst[54]
    while num_2:
        num_1, num_2 = (num_2, num_1 % num_2)
    return num_1