def composite_nums_between_indices(lst):

    def check_composite(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {lst[i] for i in range(75, 95) if check_composite(lst[i])}