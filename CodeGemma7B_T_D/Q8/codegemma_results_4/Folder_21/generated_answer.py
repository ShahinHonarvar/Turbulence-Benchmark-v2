def all_even_ints_exclusive(lst):
    result = []
    for i in range(743, 867):
        if lst[i] % 2 == 0 and i != 744:
            result.append(lst[i])
    return result