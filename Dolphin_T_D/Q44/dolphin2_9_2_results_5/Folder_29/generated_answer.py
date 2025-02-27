def composite_nums_between_indices(lst):
    return set((number for number in lst[52:72] if len(set((number // j for j in range(2, int(number ** 0.5) + 1) if number % j == 0))) > 1))