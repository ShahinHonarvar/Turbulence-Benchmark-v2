def composite_nums_between_indices(list_of_numbers):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    return set((x for i, x in enumerate(list_of_numbers[15:40], start=16) if is_composite(x)))