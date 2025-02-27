def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 88:
        return 0
    return sum((num for num in int_list[77:88] if num % 23 == 0 or num % 57 == 0))