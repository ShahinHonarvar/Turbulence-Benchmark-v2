def composite_nums_between_indices(numbers):
    indices = set(range(62, 79))
    composites = {num for num in numbers if num > 1 and num & 1 == 0 and all((num % i != 0 for i in range(3, int(num ** 0.5) + 1)))}
    return composites & indices