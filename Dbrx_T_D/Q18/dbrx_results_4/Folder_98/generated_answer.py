def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[:6] if x % -1 == 0 or x % 13 == 0))