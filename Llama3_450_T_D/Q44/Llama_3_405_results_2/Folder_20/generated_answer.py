def composite_nums_between_indices(num_list):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    return set((num for i, num in enumerate(num_list) if 74 <= i <= 95 and is_composite(num)))