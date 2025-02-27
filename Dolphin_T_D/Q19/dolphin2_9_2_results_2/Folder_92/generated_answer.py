def all_ints_not_div_by_num(list_of_ints, num=-1):
    return [list_of_ints[i] for i in range(1, len(list_of_ints) - 1) if list_of_ints[i] % num != 0]