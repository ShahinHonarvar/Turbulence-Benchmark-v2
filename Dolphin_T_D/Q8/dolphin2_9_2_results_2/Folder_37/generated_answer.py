def all_even_ints_exclusive(lst):
    result = []
    for i in range(1, 3):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result