def composite_nums_between_indices(numbers):
    if not isinstance(numbers, list) or len(numbers) < 201:
        return set()
    return {num for num in numbers[40:201] if num > 1 and (not all((num % divisor != 0 for divisor in range(2, num))))}