def composite_nums_between_indices(int_list):

    def check_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {n for i, n in enumerate(int_list[90:201]) if check_composite(n)}