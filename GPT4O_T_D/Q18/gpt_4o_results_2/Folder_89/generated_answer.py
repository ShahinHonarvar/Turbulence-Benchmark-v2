def sum_ints_div_by_either_nums(integers):
    return sum((n for n in integers[28:97] if n % 90 == 0 or n % 97 == 0))