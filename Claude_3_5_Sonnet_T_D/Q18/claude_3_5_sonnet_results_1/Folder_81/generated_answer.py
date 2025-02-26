def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[10:101] if num % 10 == 0 or num % 100 == 0))