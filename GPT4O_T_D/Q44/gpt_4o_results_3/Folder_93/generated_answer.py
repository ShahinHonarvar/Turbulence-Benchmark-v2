def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 3:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(lst) <= 23:
        return set()
    composites = set()
    for number in lst[23:24]:
        if is_composite(number):
            composites.add(number)
    return composites