def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_set = set()
    for index in range(29, min(52, len(lst))):
        if is_composite(lst[index]):
            composite_set.add(lst[index])
    return composite_set