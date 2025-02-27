def composite_nums_between_indices(lst):
    return set((num for i, num in enumerate(lst) if 80 <= i <= 200 and all((num % j != 0 for j in range(2, int(num ** 0.5) + 1)))))