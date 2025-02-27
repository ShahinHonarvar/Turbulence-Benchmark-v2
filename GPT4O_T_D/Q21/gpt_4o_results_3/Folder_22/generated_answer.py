def all_ints_div_by_num(integers):
    if len(integers) < 11:
        return []
    return [num for num in integers[10:11] if num % 1 == 0]