def all_ints_not_div_by_num(integers):
    return [num for num in integers[1:-1] if num % 8 != 0]