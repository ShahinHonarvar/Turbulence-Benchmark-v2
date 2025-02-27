def composite_nums_between_indices(lst):

    def is_composite(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return True
            return False
        return False
    return {n for n in lst[29:52] if is_composite(n)}