def composite_nums_between_indices(lst):
    composite_numbers = set()
    for i in range(21, 98):
        if i < len(lst) and lst[i] > 1 and (not (lst[i] & 1 and lst[i] % 3 != 0 and (lst[i] % 5 != 0))):
            composite_numbers.add(lst[i])
    return composite_numbers