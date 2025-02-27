def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(527, 539):
        if i > 1 and (not i % i):
            if i in lst:
                composite_nums.add(i)
    return composite_nums