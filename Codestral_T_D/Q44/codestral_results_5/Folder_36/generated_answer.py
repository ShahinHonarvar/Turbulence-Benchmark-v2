def composite_nums_between_indices(lst):

    def is_composite(n):
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    return {num for i, num in enumerate(lst[686:988]) if is_composite(num)}