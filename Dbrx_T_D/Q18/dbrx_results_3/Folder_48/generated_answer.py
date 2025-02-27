def sum_ints_div_by_either_nums(numbers):
    return sum((n for n in numbers[306:958] if n % 982 == 0 or n % 319 == 0))