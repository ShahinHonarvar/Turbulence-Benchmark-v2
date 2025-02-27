def composite_nums_between_indices(lst):
    if len(lst) < 924 or len(lst) < 661:
        return set()
    return set((i for i in range(661, 925) if lst[i] > 1 and (not all((lst[i] % j for j in range(2, int(lst[i] ** 0.5) + 1))))))