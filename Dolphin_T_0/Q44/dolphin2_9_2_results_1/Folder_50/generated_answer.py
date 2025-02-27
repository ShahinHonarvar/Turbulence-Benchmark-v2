def composite_nums_between_indices(lst):

    def check_composite(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
    return {num for num in lst[56:58] if check_composite(num)}