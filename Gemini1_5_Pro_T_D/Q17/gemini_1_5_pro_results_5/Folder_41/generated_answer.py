def all_ints_div_by_both_two_nums(list_of_ints):
    res = []
    for i in range(min(10, len(list_of_ints))):
        if list_of_ints[i] % 6 == 0 and list_of_ints[i] % -3 == 0:
            res.append(list_of_ints[i])
    return res