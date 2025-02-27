def composite_nums_between_indices(lst):
    composites = set()
    for i in range(10, 67):
        if i in lst and (not is_prime(i)):
            composites.add(i)
    return composites