def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for x in range(2, n):
            if n % x == 0:
                return True
        return False
    return set((x for x in lst[639:976] if is_composite(x)))