def composite_nums_between_indices(numbers):
    indices_range = set(range(69, 84))
    composite_numbers = {num for num in numbers if num > 1 and num % 2 != 0 and all((num % i != 0 for i in range(3, int(num ** 0.5) + 1)))}
    return indices_range.intersection(composite_numbers)