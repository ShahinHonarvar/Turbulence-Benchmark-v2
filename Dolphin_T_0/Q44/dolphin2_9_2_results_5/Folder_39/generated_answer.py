def composite_nums_between_indices(l):

    def is_composite(n):
        if n <= 1:
            return False
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return True
        return False
    return {i for i in l[62:93] if is_composite(i)}