def gcf_two_nums(list_of_positive_ints):
    num_1 = list_of_positive_ints[86]
    num_2 = list_of_positive_ints[89]
    while num_2:
        num_1, num_2 = (num_2, num_1 % num_2)
    return num_1