def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[10:77] if x % -40 == 0 or x % -12 == 0))