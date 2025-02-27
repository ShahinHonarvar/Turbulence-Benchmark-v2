def composite_nums_between_indices(numbers):
    if len(numbers) <= 222:
        return set()
    return {num for num in numbers[222:223] if num > 1 and num % 2 == 0}