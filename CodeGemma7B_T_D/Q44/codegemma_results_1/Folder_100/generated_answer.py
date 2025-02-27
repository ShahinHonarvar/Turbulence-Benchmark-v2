def composite_nums_between_indices(list):
    composites_between_indices_12_92 = set()
    for i in range(12, 93):
        if i in set(list) and i not in {2, 3, 5, 7}:
            composites_between_indices_12_92.add(i)
    return composites_between_indices_12_92