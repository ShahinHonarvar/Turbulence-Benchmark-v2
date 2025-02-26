def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[77:88] if num % 23 == 0 or num % 57 == 0))