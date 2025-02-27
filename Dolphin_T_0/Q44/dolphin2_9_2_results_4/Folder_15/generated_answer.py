def composite_nums_between_indices(lst):

    def is_composite(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        return False
    return {num for num in lst[0:4] if is_composite(num)}