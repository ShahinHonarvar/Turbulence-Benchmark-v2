def composite_nums_between_indices(numbers):
    if len(numbers) < 88:
        return set()
    composite_numbers = {num for num in numbers[25:88] if num > 1 and num % 2 == 0 and (num % 3 != 0) or (num % 2 != 0 and num > 4 and any((num % i != 0 for i in range(2, int(num ** 0.5) + 1))))}
    return composite_numbers