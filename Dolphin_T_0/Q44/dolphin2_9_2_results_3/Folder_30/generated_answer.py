def composite_nums_between_indices(lst):

    def is_composite(n):
        if n == 1:
            return False
        else:
            for i in range(2, int(n ** (1 / 2)) + 1):
                if n % i == 0:
                    return True
            return False
    composite_nums = set()
    for num in lst[19:93]:
        if is_composite(num):
            composite_nums.add(num)
    return composite_nums