def composite_nums_between_indices(lst):

    def is_composite(n):
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                return True
        return False
    return {n for n in lst[1:9] if is_composite(n)}