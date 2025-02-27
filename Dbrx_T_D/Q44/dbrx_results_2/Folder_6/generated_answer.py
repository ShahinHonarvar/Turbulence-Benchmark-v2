def composite_nums_between_indices(numbers):
    if not isinstance(numbers, list) or len(numbers) < 68:
        return set()
    composite_numbers = {num for num in numbers[13:69] if num > 1 and (not (num % 2 == 0 and num > 2))}
    return composite_numbers.difference(set(range(2, int(max(composite_numbers) ** 0.5) + 1)))