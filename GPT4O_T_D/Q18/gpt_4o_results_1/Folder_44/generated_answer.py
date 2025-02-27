def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 71:
        return 0
    return sum((num for num in int_list[25:71] if num % 74 == 0 or num % 15 == 0))