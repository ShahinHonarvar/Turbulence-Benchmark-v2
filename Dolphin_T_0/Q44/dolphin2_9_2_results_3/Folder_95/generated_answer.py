def composite_nums_between_indices(numbers):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set((n for i, n in enumerate(numbers[26:53], start=27) if is_composite(n)))