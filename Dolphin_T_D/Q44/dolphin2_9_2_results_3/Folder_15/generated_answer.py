def composite_nums_between_indices(lst):

    def is_composite(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return True
        return False
    composite_nums = set()
    for i in range(len(lst)):
        if i >= 0 and i <= 3 and is_composite(lst[i]):
            composite_nums.add(lst[i])
    return composite_nums