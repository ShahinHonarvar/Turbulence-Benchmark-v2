def composite_nums_between_indices(lst):
    if not all((isinstance(num, int) and num > 0 for num in lst)):
        raise ValueError('All elements in the list must be positive integers')
    if len(lst) < 60:
        return set()
    composite_numbers = set()
    for i in range(25, 60):
        num = lst[i]
        if num > 1 and (not (num == 2 or num % 2 == 1)):
            composite_numbers.add(num)
    return composite_numbers