def composite_nums_between_indices(numbers):
    if len(numbers) < 46:
        return set()
    composite_numbers = {num for num in numbers[36:47] if num > 1 and num % 2 == 0}
    return composite_numbers