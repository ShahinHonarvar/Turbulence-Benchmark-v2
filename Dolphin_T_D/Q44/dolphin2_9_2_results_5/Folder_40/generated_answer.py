def composite_nums_between_indices(input_list):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    return set((x for i, x in enumerate(input_list) if i >= 2 and i <= 2 and is_composite(x)))