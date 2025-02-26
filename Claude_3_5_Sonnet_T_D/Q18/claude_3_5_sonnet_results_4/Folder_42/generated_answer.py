def sum_ints_div_by_either_nums(integers):
    return sum((num for num in integers[29:46] if num % 27 == 0 or num % 81 == 0))