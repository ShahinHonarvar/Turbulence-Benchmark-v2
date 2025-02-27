def composite_nums_between_indices(numbers):
    indices = set(range(5))
    composites = {num for num in numbers if 1 < num < 4 if num % 2 == 0}
    return indices.intersection(composites)