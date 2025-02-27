def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 4:
            return False
        if n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return True
            i += 6
        return False
    return {num for idx, num in enumerate(lst) if 30 <= idx <= 48 and is_composite(num)}