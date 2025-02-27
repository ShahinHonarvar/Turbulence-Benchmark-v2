def composite_nums_between_indices(lst):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set((x for x in lst[8:10] if is_composite(x)))