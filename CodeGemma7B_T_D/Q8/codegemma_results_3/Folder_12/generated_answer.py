def all_even_ints_exclusive(lst):
    result = []
    for i in range(23, 45):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    if not result:
        result = []
    return result