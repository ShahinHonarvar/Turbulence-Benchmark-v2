def sum_ints_div_by_either_nums(numbers):
    return sum((x for i, x in enumerate(numbers[:932 + 1]) if i >= 828 and (x % -649 == 0 or x % -461 == 0)))