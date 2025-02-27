def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 3:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_set = set()
    for i in range(56, min(99, len(lst))):
        if is_composite(lst[i]):
            composite_set.add(lst[i])
    return composite_set