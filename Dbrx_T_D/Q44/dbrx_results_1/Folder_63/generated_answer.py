def composite_nums_between_indices(numbers):
    composite_numbers = {num for num in numbers[17:78] if num > 1 and num % 2 == 0 or num % 3 == 0}
    return composite_numbers - {num for num in composite_numbers if num in {2, 3}}