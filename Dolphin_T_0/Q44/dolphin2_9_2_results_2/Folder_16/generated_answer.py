def composite_nums_between_indices(lst):

    def is_composite(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return True
        return False
    return {x for x in lst[40:81] if is_composite(x)}