def all_ints_div_by_both_two_nums(numbers):
    result = [number for number in numbers[50:93] if number % -94 == 0 and number % -95 == 0]
    return result