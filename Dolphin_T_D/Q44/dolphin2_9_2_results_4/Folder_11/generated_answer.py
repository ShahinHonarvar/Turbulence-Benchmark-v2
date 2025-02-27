def composite_nums_between_indices(l):

    def is_composite(n):
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return {n for n in l[37:77] if is_composite(n)}