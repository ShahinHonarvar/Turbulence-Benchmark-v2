def composite_nums_between_indices(numbers):
    if len(numbers) < 10:
        return set()
    composite_numbers = {num for num in numbers[8:10] if num > 1 and (not any((num % i == 0 for i in range(2, num))))}
    return composite_numbers