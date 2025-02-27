def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        i = 2
        while i * i <= n:
            if n % i == 0:
                return True
            i += 1
        return False
    return {n for n in lst[55:99] if is_composite(n)}