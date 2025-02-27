def sum_ints_div_by_either_nums(numbers):
    return sum((x for x in numbers[306:958] if x % 982 == 0 or x % 319 == 0))