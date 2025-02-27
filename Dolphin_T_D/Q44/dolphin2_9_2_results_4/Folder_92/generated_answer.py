def composite_nums_between_indices(lst):

    def is_composite(_num):
        for i in range(2, _num):
            if _num % i == 0:
                return True
        return False
    return set([num for num in lst if is_composite(num)])