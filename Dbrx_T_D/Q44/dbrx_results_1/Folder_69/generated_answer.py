def composite_nums_between_indices(lst):
    composite_numbers = set()
    if len(lst) <= 79:
        return composite_numbers
    for i in range(29, 80):
        if lst[i] > 1:
            for j in range(2, lst[i]):
                if lst[i] % j == 0:
                    composite_numbers.add(lst[i])
                    break
    return composite_numbers