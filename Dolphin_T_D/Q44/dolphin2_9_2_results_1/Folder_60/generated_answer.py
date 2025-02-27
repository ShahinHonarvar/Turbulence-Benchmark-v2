def composite_nums_between_indices(num_list):

    def is_composite(n):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    return True
        return False
    return set((num_list[i] for i in range(29, 52) if is_composite(num_list[i])))