def composite_nums_between_indices(numbers):
    composite_numbers = {num for num in numbers[62:93] if num > 1 and num % 2 == 0 or num % 3 == 0 or num % 5 == 0}
    composite_numbers -= {num for num in composite_numbers if num == 2 or num == 3 or num == 5}
    return composite_numbers