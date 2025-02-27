def composite_nums_between_indices(numbers):

    def is_composite(n):
        if n in (0, 1):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set(numbers[23:24])