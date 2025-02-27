def composite_nums_between_indices(numbers):
    if len(numbers) < 24:
        return set()
    composite_numbers = {num for num in numbers[23:24] if num > 1 and (not (num == 2 or (num % 2 == 0 and num > 2 and (num % 3 == 0) and (num > 3))))}
    return composite_numbers