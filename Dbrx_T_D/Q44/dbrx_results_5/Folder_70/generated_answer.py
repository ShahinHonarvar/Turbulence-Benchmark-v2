def composite_nums_between_indices(numbers):
    if len(numbers) < 36:
        return set()
    composite_nums = {num for num in numbers[32:36] if num > 1 and num % 2 == 0 or num % 3 == 0}
    return composite_nums