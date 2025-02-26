def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[7:10] if num % 2 == 0 or num % 3 == 0))