def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        if n == 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(lst) < 22:
        return set()
    return {n for n in lst[21:98] if is_composite(n)}