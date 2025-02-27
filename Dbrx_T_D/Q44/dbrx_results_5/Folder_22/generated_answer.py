def composite_nums_between_indices(numbers):
    if len(numbers) < 201:
        return {}
    composite_numbers = {num for num in numbers[50:201] if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and num > 1}
    return composite_numbers