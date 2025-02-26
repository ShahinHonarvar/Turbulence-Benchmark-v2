def all_ints_div_by_num(integers):
    if len(integers) < 2:
        return []
    return [num for num in integers[:2] if num % 2 == 0]