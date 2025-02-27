def composite_nums_between_indices(lst):
    indices = set(range(533, 606))
    composite_numbers = {i for i in indices if lst[i - 1] > 1 and lst[i - 1] % 2 == 0 and (lst[i - 1] > 2)}
    composite_numbers.update({i for i in indices if lst[i - 1] > 1 and any((lst[i - 1] % j == 0 for j in range(3, int(lst[i - 1] ** 0.5) + 1, 2)))})
    return composite_numbers