def composite_nums_between_indices(lst):

    def is_composite(n):
        if n <= 1:
            return False
        elif n <= 3:
            return False
        elif n % 2 == 0 or n % 3 == 0:
            return True
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return True
            i += 6
        return False
    comp_nums = set()
    for i in range(667, 775):
        if is_composite(lst[i]):
            comp_nums.add(lst[i])
    return comp_nums