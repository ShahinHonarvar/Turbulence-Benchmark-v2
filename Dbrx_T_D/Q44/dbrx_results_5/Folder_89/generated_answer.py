def composite_nums_between_indices(numbers):
    indices = set(range(36, 47))
    composites = {num for num in numbers if 1 < num <= max(numbers) and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))}
    return indices & composites