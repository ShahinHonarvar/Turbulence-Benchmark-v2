def sum_ints_div_by_either_nums(integers):
    return sum((num for num in integers[10:29] if num % -61 == 0 or num % -64 == 0))