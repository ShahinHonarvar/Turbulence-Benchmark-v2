def composite_nums_between_indices(lst):

    def is_composite(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return True
            else:
                return False
        else:
            return False
    return set((num for num in lst[0:9] if is_composite(num)))