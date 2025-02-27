def all_ints_div_by_both_two_nums(list_of_ints):
    res = []
    for i in range(42, 44):
        if i < len(list_of_ints):
            if list_of_ints[i] % 15 == 0 and list_of_ints[i] % 87 == 0:
                res.append(list_of_ints[i])
    return res