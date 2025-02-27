def composite_nums_between_indices(lst):

    def is_composite(n):
        if n > 1:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return True
            return False
        return False
    return {n for n in lst if 0 <= lst.index(n) <= 3 and is_composite(n)}