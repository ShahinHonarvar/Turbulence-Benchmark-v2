def composite_nums_between_indices(lst):
    return {n for n in lst[35:50] if n > 1 and any((n % i == 0 for i in range(2, int(n ** 0.5) + 1)))}