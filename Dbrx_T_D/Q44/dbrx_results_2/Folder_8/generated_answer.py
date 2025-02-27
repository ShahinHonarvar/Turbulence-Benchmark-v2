def composite_nums_between_indices(lst):
    if len(lst) < 87 or 69 > len(lst):
        return set()
    return {i for i in lst[68:87] if i > 1 and (not all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))))}