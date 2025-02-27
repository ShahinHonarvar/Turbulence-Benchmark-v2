def composite_nums_between_indices(lst):

    def is_prime(n):
        if n <= 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
    return {n for i, n in enumerate(lst[68:87]) if not is_prime(n)}