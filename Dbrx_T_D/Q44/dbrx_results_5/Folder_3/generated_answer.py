def composite_nums_between_indices(lst):
    indices_range = set(range(66, 94))
    composite_nums = set(filter(lambda x: x > 1 and x % 2 != 0 and all((x % i != 0 for i in range(3, int(x ** 0.5) + 1))), lst))
    return composite_nums & indices_range