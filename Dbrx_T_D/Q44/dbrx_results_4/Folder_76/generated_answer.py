def composite_nums_between_indices(lst):
    if not all((isinstance(i, int) and i > 0 for i in lst)):
        raise ValueError('All elements in the list must be positive integers')
    if len(lst) < 975:
        raise IndexError('The list must have at least 975 elements')
    composite_numbers = {i for i in lst[639:976] if i > 1 and (not all((i % j for j in range(2, int(i ** 0.5) + 1))))}
    return composite_numbers