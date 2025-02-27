def composite_nums_between_indices(lst):

    def check_composite(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    return set([x for x in lst[29:80] if check_composite(x)])