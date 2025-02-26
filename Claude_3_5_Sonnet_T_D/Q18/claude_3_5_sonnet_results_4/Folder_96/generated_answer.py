def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[50:201] if num % -34 == 0 or num % 64 == 0))