def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst, 1) if 1 <= i <= 5 and all((num % j != 0 for j in range(2, int(num ** 0.5) + 1)))}