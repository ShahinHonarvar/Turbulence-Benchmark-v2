def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[70:201] if num % 3 == 0 or num % -300 == 0))