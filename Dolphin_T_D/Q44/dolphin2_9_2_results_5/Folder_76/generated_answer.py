def composite_nums_between_indices(lst):

    def is_composite(n):
        if n in (0, 1):
            return False
        if n % 2 == 0:
            return True
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return True
        return False
    return {n for n in lst[639:976] if is_composite(n)}