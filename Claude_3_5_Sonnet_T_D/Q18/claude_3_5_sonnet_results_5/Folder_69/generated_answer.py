def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[61:89] if num % 31 == 0 or num % 11 == 0))