def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 4:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(lst) <= 1:
        return set()
    composite_numbers = set()
    if is_composite(lst[1]):
        composite_numbers.add(lst[1])
    return composite_numbers