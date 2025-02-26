def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[3:10] if num % 6 == 0 or num % 1 == 0))