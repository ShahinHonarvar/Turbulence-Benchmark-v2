def composite_nums_between_indices(lst):
    return {num for i, num in enumerate(lst[35:50], 35) if all((num % j != 0 for j in range(2, num)))}