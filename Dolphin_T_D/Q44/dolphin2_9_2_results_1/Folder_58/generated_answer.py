def composite_nums_between_indices(lst):

    def is_composite(n):
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return {n for n in lst[533:606] if is_composite(n)}