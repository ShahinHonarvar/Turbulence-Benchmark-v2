def composite_nums_between_indices(numbers):
    indices = set(range(42, 69))
    return {num for num in numbers if num in indices and num > 1 and (num % 2 == 0)}