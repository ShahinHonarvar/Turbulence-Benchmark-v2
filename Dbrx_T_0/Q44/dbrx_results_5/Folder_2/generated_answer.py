def composite_nums_between_indices(numbers):
    if len(numbers) < 50:
        return set()
    composite_numbers = {num for num in numbers[35:50] if num > 1 and num % 2 == 0 or num % 3 == 0 or num % 5 == 0}
    return composite_numbers - {2, 3, 5}