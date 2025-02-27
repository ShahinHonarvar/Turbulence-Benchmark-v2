def composite_nums_between_indices(numbers):
    composite_numbers = {num for num in numbers[51:87] if num > 1 and num % 2 == 0 or num % 3 == 0 or num % 5 == 0}
    return composite_numbers