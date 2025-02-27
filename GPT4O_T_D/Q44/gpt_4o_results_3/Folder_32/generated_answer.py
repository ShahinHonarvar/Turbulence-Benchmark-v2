def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        if n <= 3:
            return False
        if n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return True
            i += 6
        return False
    start, end = (10, 66)
    composites = set()
    for i in range(start, min(end + 1, len(lst))):
        if is_composite(lst[i]):
            composites.add(lst[i])
    return composites