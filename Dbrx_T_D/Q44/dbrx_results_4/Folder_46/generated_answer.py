def composite_nums_between_indices(lst):
    indices = set(range(28, 39))
    composites = {num for num in lst if num > 1 and num % 2 != 0 and all((num % i != 0 for i in range(3, int(num ** 0.5) + 1)))}
    return composites & indices if composites else set()