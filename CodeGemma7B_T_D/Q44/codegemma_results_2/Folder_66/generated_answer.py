def composite_nums_between_indices(lst):
    composites = set()
    if not 60 < len(lst) <= 64:
        return composites
    for i in lst[62:64]:
        if i > 1 and all((i % x != 0 for x in range(2, int(i ** 0.5) + 1))):
            composites.add(i)
    return composites