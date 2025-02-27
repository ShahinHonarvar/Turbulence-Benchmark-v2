def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 3:
            return n != 2 and n != 3
        if n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return True
            i += 6
        return False
    return {num for num in lst[314:348] if is_composite(num)}