def composite_nums_between_indices(lst):

    def is_composite(num):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return True
            else:
                return False
        else:
            return False
    return set(filter(is_composite, lst[55:99]))