def composite_nums_between_indices(lst):
    if len(lst) <= 23:
        return set()
    composite_numbers = {i for i in lst[23:24] if i > 1 and i % 2 == 0}
    composite_numbers.update({num for num in lst[24:] if num > 1 and num % 2 == 0 and (num in composite_numbers)})
    composite_numbers.update({num for num in lst[23::-1] if num > 1 and num % 2 == 0 and (num in composite_numbers)})
    return composite_numbers