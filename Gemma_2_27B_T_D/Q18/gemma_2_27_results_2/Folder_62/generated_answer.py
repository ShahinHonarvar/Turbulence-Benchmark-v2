def sum_ints_div_by_either_nums(data):
    return sum((x for x in data[44:60] if x % 39 == 0 or x % 15 == 0))