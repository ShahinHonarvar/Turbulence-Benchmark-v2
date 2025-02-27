def composite_nums_between_indices(lst):

    def is_composite(n):
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    indices = range(56, 58)
    composites = set((x for i, x in enumerate(lst, 1) if i in indices and is_composite(x)))
    return composites