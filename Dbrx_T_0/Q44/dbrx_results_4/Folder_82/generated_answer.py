def composite_nums_between_indices(numbers):
    if len(numbers) < 31:
        return set()
    composite_numbers = {num for num in numbers[30:31] if num > 1 and (not (num == 2 or (num % 2 == 0 and num % 3 == 0) or (num % 2 != 0 and (num - 2) % 3 == 0)))}
    return composite_numbers