def composite_nums_between_indices(lst):

    def is_composite(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return True
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return True
        return False
    return {num for num in lst[12:93] if is_composite(num)}