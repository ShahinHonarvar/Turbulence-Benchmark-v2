def composite_nums_between_indices(num_list):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, np.int(np.sqrt(n)) + 1):
            if n % i == 0:
                return True
        return False
    return set((x for i, x in enumerate(num_list[52:72], 52) if is_composite(x)))