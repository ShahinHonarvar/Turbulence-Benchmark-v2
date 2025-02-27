def composite_nums_between_indices(numbers):
    if len(numbers) < 2:
        return set()
    return {num for num in numbers[1:6] if num > 1 and num % 2 == 0 or num % 3 == 0 or num % 5 == 0}