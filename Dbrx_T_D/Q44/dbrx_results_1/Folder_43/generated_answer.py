def composite_nums_between_indices(numbers):
    indices = set(range(31, 73))
    composites = {num for num in numbers if not num % 2 and num != 2 or (any((num % i == 0 for i in range(3, int(num ** 0.5) + 1))) and num in indices)}
    return composites