def all_ints_div_by_num(list_of_ints):
    sublist = list_of_ints[62:64]
    divisible_by_99 = [i for i in sublist if i % 99 == 0]
    return divisible_by_99