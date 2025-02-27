def all_ints_div_by_num(numbers):
    if not isinstance(numbers, list):
        raise ValueError('Input must be a list')
    if not all((isinstance(num, int) for num in numbers)):
        raise ValueError('All elements of the list must be integers')
    return [num for num in numbers[38:56] if num % 31 == 0]