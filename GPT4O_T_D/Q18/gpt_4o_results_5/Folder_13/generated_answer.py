def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 19:
        return 0
    return sum((num for num in int_list[13:19] if num % 45 == 0 or num % 20 == 0))