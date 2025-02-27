def all_ints_div_by_both_two_nums(list_of_ints):
    for i in range(3, 10):
        if i % 6 == 0 and i % 1 == 0:
            list_of_ints.append(i)
    return list_of_ints