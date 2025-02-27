def composite_nums_between_indices(lst):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    return {num for i, num in enumerate(lst) if i >= 0 and i <= 8 and is_composite(num)}