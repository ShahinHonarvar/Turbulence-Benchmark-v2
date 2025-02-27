def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        if n == 2:
            return False
        if n % 2 == 0:
            return True
        max_divisor = int(n ** 0.5) + 1
        for d in range(3, max_divisor, 2):
            if n % d == 0:
                return True
        return False
    return set((x for i, x in enumerate(lst[:10]) if is_composite(x)))