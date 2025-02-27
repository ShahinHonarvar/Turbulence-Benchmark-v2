def composite_nums_between_indices(numbers):
    indices = set(range(59, 98))
    composites = {num for num in numbers if num > 1 and num % 2 == 0 or num % 3 == 0}
    return indices.intersection(composites)