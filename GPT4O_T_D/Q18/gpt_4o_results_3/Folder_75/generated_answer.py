def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 21:
        return 0
    return sum((num for num in int_list[20:94] if num % -92 == 0 or num % -50 == 0))