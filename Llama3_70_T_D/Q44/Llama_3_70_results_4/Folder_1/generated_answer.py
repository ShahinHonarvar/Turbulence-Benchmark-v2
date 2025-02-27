def composite_nums_between_indices(num_list):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set((num for i, num in enumerate(num_list) if 69 <= i <= 83 and is_composite(num)))