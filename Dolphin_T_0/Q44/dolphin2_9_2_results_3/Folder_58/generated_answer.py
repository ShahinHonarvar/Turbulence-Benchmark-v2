def composite_nums_between_indices(num_list):

    def is_composite(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return True
            else:
                return False
        else:
            return False
    return set((num for i, num in enumerate(num_list[533:606]) if composite_nums_between_indices(num)))