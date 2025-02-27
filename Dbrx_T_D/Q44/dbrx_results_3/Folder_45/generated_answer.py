def composite_nums_between_indices(numbers):
    if len(numbers) < 201 or len(numbers) < 41:
        return set()
    return {num for num in numbers[41:201] if num > 1 and num % 2 == 0 or num % 3 == 0 or num % 5 == 0}