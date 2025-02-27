def composite_nums_between_indices(numbers):
    if len(numbers) < 58:
        return set()
    composite_numbers = {num for num in numbers[56:58] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_numbers