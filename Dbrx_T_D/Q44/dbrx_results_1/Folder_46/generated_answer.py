def composite_nums_between_indices(numbers):
    composite_numbers = set(filter(lambda x: x > 1 and x % 2 == 0 or x % 3 == 0, numbers))
    return composite_numbers & set(range(numbers[28], numbers[39]))