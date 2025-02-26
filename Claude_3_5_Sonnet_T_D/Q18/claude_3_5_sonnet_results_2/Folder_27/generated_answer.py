def sum_ints_div_by_either_nums(integers):
    return sum((num for num in integers[20:36] if num % -36 == 0 or num % -89 == 0))