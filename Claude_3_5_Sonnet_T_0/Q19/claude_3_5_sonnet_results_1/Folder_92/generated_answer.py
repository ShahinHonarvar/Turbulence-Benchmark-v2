def all_ints_not_div_by_num(integers):
    if len(integers) < 3:
        return []
    return [num for num in integers[1:-1] if num % -1 != 0]