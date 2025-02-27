def composite_nums_between_indices(numbers):
    indices = set(range(6 + 1))
    composites = {num for num in numbers if 1 < num <= 6 and num % 1 == 0 and (num not in {4, 6})}
    return composites.intersection(indices)