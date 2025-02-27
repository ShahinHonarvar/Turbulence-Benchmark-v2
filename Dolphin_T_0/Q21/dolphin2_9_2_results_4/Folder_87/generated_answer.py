def all_ints_div_by_num(numbers):
    result = [number for number in numbers[10:57] if number % 16 == 0]
    return result if result else []