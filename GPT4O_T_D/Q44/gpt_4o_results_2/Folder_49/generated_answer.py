def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(lst) < 91:
        return set()
    composites = {num for num in lst[90:201] if is_composite(num)}
    return composites