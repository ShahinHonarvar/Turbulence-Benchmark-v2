def composite_nums_between_indices(lst):
    composite_numbers = set()
    for i in range(90, 201):
        if lst[i] > 1:
            for j in range(2, lst[i]):
                if lst[i] % j == 0:
                    composite_numbers.add(lst[i])
    return composite_numbers