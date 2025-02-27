def all_ints_div_by_both_two_nums(list_of_ints):
    return [num for i in range(38, 82) if i < len(list_of_ints) and list_of_ints[i] % -61 == 0 and (list_of_ints[i] % -71 == 0)]