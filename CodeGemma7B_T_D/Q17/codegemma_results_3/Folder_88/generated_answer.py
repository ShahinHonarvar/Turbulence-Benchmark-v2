def all_ints_div_by_both_two_nums(int_list):
    new_list = []
    for i in range(3, 10):
        if i in int_list:
            if i % 6 == 0 and i % 1 == 0:
                new_list.append(i)
    return new_list