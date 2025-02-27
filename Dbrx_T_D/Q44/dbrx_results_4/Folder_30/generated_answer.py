def composite_nums_between_indices(numbers):
    indices = set(range(19, 93))
    composites = {num for num in numbers if 1 < num < 100 and num % 2 == 0 or (num - 1) % 6 == 0}
    return composites.intersection(indices)