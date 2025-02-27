def composite_nums_between_indices(numbers):
    if len(numbers) < 24:
        return set()
    composite_numbers = {num for num in numbers[23:24] if num > 1 and (not num == 2) and any((num % i == 0 for i in range(2, num)))}
    return composite_numbers