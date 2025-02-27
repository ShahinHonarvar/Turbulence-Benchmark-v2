def composite_nums_between_indices(numbers):
    if not isinstance(numbers, list) or not all((isinstance(num, int) and num > 0 for num in numbers)):
        raise ValueError('Input must be a list of positive integers')
    composite_numbers = {num for num in numbers[62:93] if num > 1 and (not all((num % divisor != 0 for divisor in range(2, num))))}
    return composite_numbers