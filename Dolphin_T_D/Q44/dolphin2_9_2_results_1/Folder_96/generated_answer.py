def composite_nums_between_indices(lst):

    def is_composite(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return True
        return False
    indices = lst[60:201]
    composite_nums = set()
    for i in indices:
        if is_composite(i):
            composite_nums.add(i)
    return composite_nums