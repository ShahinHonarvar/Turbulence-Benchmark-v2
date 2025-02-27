def composite_nums_between_indices(lst):

    def is_composite(num):
        if num < 4:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    if len(lst) < 3:
        return set()
    composites = set()
    if is_composite(lst[2]):
        composites.add(lst[2])
    return composites