def sum_ints_div_by_either_nums(int_list):
    if len(int_list) > 7:
        number = int_list[7]
        if number % 5 == 0 or number % 7 == 0:
            return number
    return 0