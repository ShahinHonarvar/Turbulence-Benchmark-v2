def composite_nums_between_indices(lst):

    def is_composite(n):
        if n in (0, 1) or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True
    return set((n for n in lst[0:5] if is_composite(n)))