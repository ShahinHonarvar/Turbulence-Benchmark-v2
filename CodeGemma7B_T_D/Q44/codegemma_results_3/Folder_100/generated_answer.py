def composite_nums_between_indices(lst):
    composite_set = set()
    for num in lst[12:93]:
        if num % 2 == 0 or num % 3 == 0:
            composite_set.add(num)
    return composite_set