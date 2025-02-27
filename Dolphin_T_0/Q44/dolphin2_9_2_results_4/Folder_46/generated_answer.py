def composite_nums_between_indices(lst):

    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return set((n for n in lst[28:39] if check_composite(n)))