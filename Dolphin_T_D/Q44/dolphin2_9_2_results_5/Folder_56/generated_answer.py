def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composites = set()
    for i in lst[0:1]:
        if is_composite(i):
            composites.add(i)
    return composites