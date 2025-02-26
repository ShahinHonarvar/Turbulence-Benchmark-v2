def sum_ints_div_by_either_nums(integers):
    return sum((num for num in integers[55:85] if num % -24 == 0 or num % -11 == 0))