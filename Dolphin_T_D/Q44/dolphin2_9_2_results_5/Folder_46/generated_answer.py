def composite_nums_between_indices(lst):

    def is_composite(num):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    return True
            else:
                return False
        else:
            return False
    return set((num for num in lst[28:39] if is_composite(num)))