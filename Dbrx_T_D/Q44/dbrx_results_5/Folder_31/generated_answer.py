def composite_nums_between_indices(lst):
    if not all((isinstance(i, int) and i > 0 for i in lst)):
        raise ValueError('All elements in the list must be positive integers')
    composite_nums = set()
    for idx, num in enumerate(lst[56:67]):
        if idx == 0 or idx == 1:
            continue
        if num > 1 and all((num % i != 0 for i in range(2, num))):
            composite_nums.add(num)
    return composite_nums