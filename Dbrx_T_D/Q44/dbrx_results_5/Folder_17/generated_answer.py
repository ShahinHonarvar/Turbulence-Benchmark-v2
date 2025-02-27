def composite_nums_between_indices(numbers):
    if len(numbers) < 55:
        return set()
    return {num for num in numbers[50:55] if num > 1 and (not any((num % divisor == 0 for divisor in range(2, num))))}