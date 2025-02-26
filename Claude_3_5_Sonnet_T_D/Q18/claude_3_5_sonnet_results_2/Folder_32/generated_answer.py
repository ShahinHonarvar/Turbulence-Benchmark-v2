def sum_ints_div_by_either_nums(integers):
    return sum((num for num in integers[25:96] if num % 51 == 0 or num % 77 == 0))