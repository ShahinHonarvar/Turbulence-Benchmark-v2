def composite_nums_between_indices(lst):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    return set([num for idx, num in enumerate(lst) if 56 <= idx <= 82 and is_composite(num)])