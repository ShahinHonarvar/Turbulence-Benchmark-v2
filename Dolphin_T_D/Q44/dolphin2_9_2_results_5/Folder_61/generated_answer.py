def composite_nums_between_indices(lst):

    def is_composite(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False

    def get_nums_between_indices(lst, start, end):
        return set(lst[start:end + 1])
    return {x for x in get_nums_between_indices(lst, 0, 7) if is_composite(x)}