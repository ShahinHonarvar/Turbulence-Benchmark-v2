def composite_nums_between_indices(numbers):
    if len(numbers) < 80:
        return set()
    composite_numbers = {num for num in numbers[40:81] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_numbers