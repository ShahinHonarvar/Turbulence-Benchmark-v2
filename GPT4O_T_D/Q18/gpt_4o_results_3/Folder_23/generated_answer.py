def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 98:
        return 0
    return sum((num for num in int_list[69:98] if num % -90 == 0 or num % -67 == 0))