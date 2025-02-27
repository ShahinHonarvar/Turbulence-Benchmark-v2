def composite_nums_between_indices(lst):

    def is_composite(n):
        if n in (2, 3):
            return False
        if n % 2 == 0 or n == 1:
            return True
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return True
        return False
    return set((num for num in lst[82:87] if is_composite(num)))