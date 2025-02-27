def sum_ints_div_by_either_nums(ls):
    return sum((num for num in ls[34:82] if num % 27 == 0 or num % 57 == 0))