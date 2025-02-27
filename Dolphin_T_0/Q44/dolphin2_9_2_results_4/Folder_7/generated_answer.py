def composite_nums_between_indices(lst):

    def is_composite(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return True
        return False
    composite_nums = set()
    for num in lst[527:539]:
        if is_composite(num):
            composite_nums.add(num)
    return composite_nums