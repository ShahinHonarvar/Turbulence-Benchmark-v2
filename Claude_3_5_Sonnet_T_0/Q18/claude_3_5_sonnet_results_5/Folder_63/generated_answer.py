def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[31:51] if num % 81 == 0 or num % 64 == 0))