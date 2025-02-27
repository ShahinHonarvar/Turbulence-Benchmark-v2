from math import sqrt

def composite_nums_between_indices(lst):
    composites = set()
    for i in range(27, 56):
        if lst[i] > 1 and sum((i % j == 0 for j in range(2, int(sqrt(lst[i])) + 1))) > 1:
            composites.add(lst[i])
    return composites