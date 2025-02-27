def composite_nums_between_indices(numbers):
    indices = set(range(6, 8))
    composite_numbers = {num for num in numbers if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1)))}
    return composite_numbers.intersection(indices)