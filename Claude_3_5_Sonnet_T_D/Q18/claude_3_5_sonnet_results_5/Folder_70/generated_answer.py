def sum_ints_div_by_either_nums(integer_list):
    if len(integer_list) < 44:
        return 0
    return sum((num for num in integer_list[42:44] if num % 15 == 0 or num % 87 == 0))