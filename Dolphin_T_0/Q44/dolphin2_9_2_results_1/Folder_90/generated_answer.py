import sympy

def composite_nums_between_indices(lst):
    return set((sympy.compositor(lst[i]) for i in range(333, 369)))