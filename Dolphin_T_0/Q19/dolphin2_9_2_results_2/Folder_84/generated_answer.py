def all_ints_not_div_by_num(numbers):
    result = [number for number in numbers[50:81] if number % 64 != 0]
    return result