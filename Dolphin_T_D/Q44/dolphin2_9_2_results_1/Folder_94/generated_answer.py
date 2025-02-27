def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    filtered = [is_composite(num) for num in lst[27:56]]
    return set(lst[27:56 + 1][filtered])