def composite_nums_between_indices(numbers):
    if len(numbers) < 8:
        return set()
    composite_numbers = {num for num in numbers[1:9] if num > 1 and (not any((num % div == 0 for div in range(2, num))))}
    return composite_numbers