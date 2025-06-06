def composite_nums_between_indices(numbers):
    if len(numbers) < 72:
        return {}
    composite_numbers = {num for num in numbers[31:73] if num > 1 and (not num == 2) and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1)))}
    return composite_numbers