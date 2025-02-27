def composite_nums_between_indices(lst):
    """Returns a set composite numbers in the given list that are between index 42 to 68 (both inclusive)."""

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return set((num for i, num in enumerate(lst[42:69], 42) if is_composite(num)))