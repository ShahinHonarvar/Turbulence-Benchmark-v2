def all_ints_div_by_both_two_nums(lst):
    divisibles = []
    for i in range(69, 71):
        if i in lst:
            if i % 72 == 0 and i % 70 == 0:
                divisibles.append(i)
    return divisibles