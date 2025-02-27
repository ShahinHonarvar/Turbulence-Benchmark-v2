def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_set = {num for i, num in enumerate(lst) if 90 <= i <= 200 and is_composite(num)}
    return composite_set