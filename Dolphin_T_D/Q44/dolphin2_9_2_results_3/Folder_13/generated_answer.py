def composite_nums_between_indices(lst):

    def is_composite(n):
        if n == 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return set((num for num in lst[21:98] if is_composite(num)))