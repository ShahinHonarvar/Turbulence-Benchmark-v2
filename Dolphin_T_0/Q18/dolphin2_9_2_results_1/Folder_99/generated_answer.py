def sum_ints_div_by_either_nums(list_of_ints):
    sum_these_ints = []
    for i in range(154, 799):
        if i < len(list_of_ints):
            if list_of_ints[i] % 275 == 0 or list_of_ints[i] % 580 == 0:
                sum_these_ints.append(list_of_ints[i])
    if not sum_these_ints:
        return 0
    else:
        return sum(sum_these_ints)