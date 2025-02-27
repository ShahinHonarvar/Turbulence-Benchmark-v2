def all_even_ints_exclusive(lst):
    result = []
    for i in range(4, 6):
        if i % 2 == 0:
            result.append(lst[i])
    return result