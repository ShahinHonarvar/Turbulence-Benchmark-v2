def all_ints_div_by_both_two_nums(numbers):
    result = [number for number in numbers[306:958] if number % 982 == 0 and number % 319 == 0]
    return result