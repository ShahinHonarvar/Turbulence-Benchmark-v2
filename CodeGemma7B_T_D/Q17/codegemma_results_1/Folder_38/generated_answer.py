def all_ints_div_by_both_two_nums(list):
    all_ints = []
    for i in list:
        if i >= 10 and i <= 76:
            if i % -40 == 0 and i % -12 == 0:
                all_ints.append(i)
    return all_ints