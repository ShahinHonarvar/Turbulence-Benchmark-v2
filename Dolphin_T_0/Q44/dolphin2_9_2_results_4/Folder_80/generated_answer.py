def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return True
        return False
    return {n for n in lst[62:79] if is_composite(n)}