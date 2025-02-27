def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        elif n == 2 or n == 3:
            return False
        elif n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return True
            i += w
            w = 6 - w
        return False
    return {num for num in lst[333:369] if is_composite(num)}