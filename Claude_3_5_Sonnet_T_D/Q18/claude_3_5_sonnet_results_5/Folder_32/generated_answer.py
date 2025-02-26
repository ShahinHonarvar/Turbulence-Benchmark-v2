def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[25:96] if num % 51 == 0 or num % 77 == 0))