def composite_nums_between_indices(lst):

    def is_composite(n):
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return {lst[i] for i in range(30, 49) if is_composite(lst[i])}