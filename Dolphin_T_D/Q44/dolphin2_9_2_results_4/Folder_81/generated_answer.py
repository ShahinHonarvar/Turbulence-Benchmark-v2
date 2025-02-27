def composite_nums_between_indices(lst):

    def is_composite(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    return {lst[i] for i in range(20, 201) if is_composite(lst[i])}