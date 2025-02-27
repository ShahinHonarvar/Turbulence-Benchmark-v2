def composite_nums_between_indices(numbers):
    if len(numbers) < 89:
        return set()
    composite_numbers = {num for num in numbers[22:89] if num > 1 and num % 2 == 0 and (num != 2) or num % 3 == 0}
    return composite_numbers