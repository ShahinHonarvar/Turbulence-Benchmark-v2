def sum_ints_div_by_either_nums(int_list):
    if not int_list or len(int_list) < 77:
        return 0
    return sum((num for num in int_list[10:77] if num % -40 == 0 or num % -12 == 0))