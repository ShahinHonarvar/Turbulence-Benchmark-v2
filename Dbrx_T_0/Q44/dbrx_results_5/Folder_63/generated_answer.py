def composite_nums_between_indices(numbers):
    if len(numbers) < 78:
        return set()
    composite_numbers = {num for num in numbers[17:79] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_numbers