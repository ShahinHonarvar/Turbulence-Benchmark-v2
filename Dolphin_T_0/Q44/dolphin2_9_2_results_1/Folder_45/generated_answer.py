def composite_nums_between_indices(integer_list):

    def is_composite(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set((n for n in integer_list[40:201] if is_composite(n)))