def all_ints_div_by_num(numbers):
    result = [num for num in numbers[26:75] if num % 80 == 0]
    return result if result else []