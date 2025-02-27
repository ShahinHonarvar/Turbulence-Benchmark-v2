def composite_nums_between_indices(numbers):
    if len(numbers) < 6:
        return set()
    composite_numbers = {num for num in numbers[3:6] if num > 1 and num % 2 == 0}
    return composite_numbers