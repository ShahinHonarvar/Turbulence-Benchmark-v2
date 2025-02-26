def all_ints_div_by_num(integers):
    if len(integers) <= 20:
        return []
    return [num for num in integers[20:21] if num % 2 == 0]