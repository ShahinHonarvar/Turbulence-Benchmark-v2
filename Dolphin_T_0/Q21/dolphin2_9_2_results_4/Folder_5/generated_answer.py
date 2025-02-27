def all_ints_div_by_num(list_of_ints):
    divisible_ints = [list_of_ints[i] for i in range(1, 5) if list_of_ints[i] % -6 == 0]
    return divisible_ints