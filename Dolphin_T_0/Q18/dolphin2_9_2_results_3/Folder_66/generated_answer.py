def sum_ints_div_by_either_nums(list_of_ints):
    return sum((list_of_ints[57:82] for i in list_of_ints[57:82] if i % 55 == 0 or i % 10 == 0)) or 0