def all_even_ints_inclusive(lst):
    results = []
    for i in range(0, 9):
        if lst[i] % 2 == 0:
            results.append(lst[i])
    return results