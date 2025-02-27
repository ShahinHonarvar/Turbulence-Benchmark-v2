def composite_nums_between_indices(lst):

    def is_composite(num):
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    return set((x for x in lst[40:81] if is_composite(x)))