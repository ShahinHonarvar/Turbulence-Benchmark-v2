def composite_nums_between_indices(numbers):
    if len(numbers) < 67:
        return set()
    composite_numbers = {num for num in numbers[56:67] if num > 1 and num % 2 == 0 and (num != 2) or (num % 3 == 0 and num != 3) or (num % 5 == 0 and num != 5)}
    return composite_numbers