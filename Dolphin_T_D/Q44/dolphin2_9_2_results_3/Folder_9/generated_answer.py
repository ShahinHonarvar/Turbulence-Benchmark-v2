def composite_nums_between_indices(int_list):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    return set((num for i, num in enumerate(int_list) if 80 <= i <= 200 and is_composite(num)))