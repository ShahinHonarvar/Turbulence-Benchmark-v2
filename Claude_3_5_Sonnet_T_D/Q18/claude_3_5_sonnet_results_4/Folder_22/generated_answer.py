def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[40:201] if num % 21 == 0 or num % 71 == 0))