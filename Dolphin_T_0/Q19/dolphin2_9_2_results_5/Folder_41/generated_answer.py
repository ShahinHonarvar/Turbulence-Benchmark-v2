def all_ints_not_div_by_num(numbers):
    return [number for number in numbers[1:-1] if number % -3 != 0]