def composite_nums_between_indices(numbers):
    if len(numbers) < 69:
        return set()
    composite_numbers = {num for num in numbers[42:69] if not (num == 1 or num == 2 or (num % 2 == 0 and num != 2))}
    return composite_numbers