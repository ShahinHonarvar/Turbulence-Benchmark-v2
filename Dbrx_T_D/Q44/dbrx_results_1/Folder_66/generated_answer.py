def composite_nums_between_indices(numbers):
    indices = set(range(62, 64))
    composites = {num for num in numbers[62:64] if num > 1 and num % 2 == 0 or num % 3 == 0}
    return composites.intersection(indices)