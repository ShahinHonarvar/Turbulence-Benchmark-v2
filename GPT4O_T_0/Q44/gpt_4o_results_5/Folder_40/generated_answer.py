def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {n for n in lst[2:3] if is_composite(n)}