def composite_nums_between_indices(lst):
    return {num for num in lst[533:606] if not all((num % k for k in range(2, num))) and num != 1}