def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 8:
        return 0
    return sum((num for num in int_list[7:8] if num % 5 == 0 or num % 7 == 0))