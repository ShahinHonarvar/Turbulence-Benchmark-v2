def composite_nums_between_indices(int_list):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    return {num for num in int_list[0:7] if is_composite(num)}