def composite_nums_between_indices(lst):
    if not all((isinstance(num, int) and num > 0 for num in lst)):
        raise ValueError('All elements in the list must be positive integers')
    composite_nums = {num for num in lst[37:77] if num > 1 and (not all((num % i for i in range(2, num))))}
    return composite_nums