def composite_nums_between_indices(numbers):
    indices = set(range(70, 201))
    composites = {num for num in numbers if 1 < num <= len(numbers) and len(set((divmods(num, i)[1] for i in range(2, num))) & indices) > 0}
    return composites