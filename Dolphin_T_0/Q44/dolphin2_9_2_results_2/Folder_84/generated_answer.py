def composite_nums_between_indices(array):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set((i for i in array[30:49] if is_composite(i)))