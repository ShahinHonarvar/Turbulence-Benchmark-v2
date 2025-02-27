def all_ints_div_by_num(numbers):
    result = [num for num in numbers[57:68] if num % 90 == 0]
    return result if len(result) > 0 else []