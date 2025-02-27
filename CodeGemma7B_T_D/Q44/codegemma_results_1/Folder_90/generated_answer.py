def composite_nums_between_indices(l):
    s = set()
    for i in range(333, 369):
        if l[i] in [j for j in l[i + 1:] if not j.isnumeric() or int(j) <= 1 or int(j) in (2, 3)]:
            s.add(l[i])
    return s