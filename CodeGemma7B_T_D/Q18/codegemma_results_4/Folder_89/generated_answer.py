def sum_ints_div_by_either_nums(list_ints):
    return sum((i for i in list_ints[28:97] if i % 97 == 0 or i % 90 == 0))