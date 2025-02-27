def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst, 1) if 62 <= i <= 99 and any((num % j == 0 for j in range(2, int(num ** 0.5) + 1)))}