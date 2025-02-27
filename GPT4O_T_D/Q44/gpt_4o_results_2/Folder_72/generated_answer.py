def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(lst) <= 55:
        return set()
    result = set()
    for i in range(55, min(99, len(lst))):
        if is_composite(lst[i]):
            result.add(lst[i])
    return result