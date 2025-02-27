def composite_nums_between_indices(numbers):
    indices = set(range(55, 99))
    composite_numbers = {num for num in numbers if num > 1 and all((num % i != 0 for i in range(2, num)))}
    return indices & composite_numbers