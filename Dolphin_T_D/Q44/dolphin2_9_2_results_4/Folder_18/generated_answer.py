def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return {num for i, num in enumerate(lst) if 25 <= i <= 87 and is_composite(num)}