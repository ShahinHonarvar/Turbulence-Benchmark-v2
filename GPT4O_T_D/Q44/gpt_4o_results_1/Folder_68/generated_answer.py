def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 3:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    if len(lst) < 9:
        lst = lst[:len(lst)]
    else:
        lst = lst[:9]
    return {num for num in lst if is_composite(num)}