def composite_nums_between_indices(numbers):
    if len(numbers) < 69 or len(numbers) < 43:
        return set()
    return {num for num in numbers[42:69] if num > 1 and (not any((num % i == 0 for i in range(2, num))))}