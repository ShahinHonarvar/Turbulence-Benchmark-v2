def all_ints_not_div_by_num(numbers):
    if not isinstance(numbers, list):
        return 'Input must be a list'
    start, end = (22, 97)
    result = [num for num in numbers[start:end] if num % -46 != 0]
    return result