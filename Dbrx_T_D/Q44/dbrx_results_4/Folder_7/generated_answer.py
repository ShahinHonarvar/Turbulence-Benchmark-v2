def composite_nums_between_indices(lst):
    return {i for i in set(lst[527:539]) if i > 1 and (not all((i % j for j in range(2, i))))} if lst else set()