def composite_nums_between_indices(lst):
    composite_set = set()
    for i in range(667, 775):
        n = lst[i]
        if n < 2:
            continue
        for j in range(2, int(n ** 0.5) + 1):
            if n % j == 0:
                composite_set.add(n)
                break
    return composite_set