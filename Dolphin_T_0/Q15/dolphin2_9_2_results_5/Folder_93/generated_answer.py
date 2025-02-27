def sum_odd_ints_inclusive(lst):
    subset = lst[75:95]
    total = 0
    for i in subset:
        if i % 2 != 0:
            total += i
    return total