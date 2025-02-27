def gcf_two_nums(lst):
    num_1 = lst[66]
    num_2 = lst[90]
    while num_1 != num_2:
        if num_1 > num_2:
            num_1 -= num_2
        elif num_2 > num_1:
            num_2 -= num_1
    return num_1