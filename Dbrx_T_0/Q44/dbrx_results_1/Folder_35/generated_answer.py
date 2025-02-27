def composite_nums_between_indices(numbers):
    if len(numbers) < 33:
        return set()
    composite_numbers = {num for num in numbers[28:33] if num > 1 and num % 2 == 0}
    return composite_numbers