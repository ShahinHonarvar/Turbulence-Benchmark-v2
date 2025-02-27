def all_ints_div_by_num(numbers):
    result = [num for num in numbers[45:81] if num % 39 == 0]
    return result if len(result) > 0 else []