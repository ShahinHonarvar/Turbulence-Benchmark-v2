def all_ints_not_div_by_num(numbers):
    start, end = (22, 97)
    return [num for num in numbers[start:end:1] if num % -46 != 0]