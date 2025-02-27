def composite_nums_between_indices(lst):

    def is_composite(n):
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return set((x for x in lst[75:89] if is_composite(x)))