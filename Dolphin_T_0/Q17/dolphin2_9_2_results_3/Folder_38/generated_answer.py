def all_ints_div_by_both_two_nums(lst):
    found = []
    for i in range(10, 76 + 1):
        if i % -40 == 0 and i % -12 == 0:
            found.append(i)
    return found