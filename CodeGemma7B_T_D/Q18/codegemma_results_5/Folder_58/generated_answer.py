def sum_ints_div_by_either_nums(int_list):
    if not int_list[240:902]:
        return 0
    else:
        return sum([num for num in int_list[240:902] if num % 546 == 0 or num % 709 == 0])