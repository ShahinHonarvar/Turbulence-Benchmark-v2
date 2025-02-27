def all_even_ints_exclusive(lst):
    result = []
    for i in range(max(6, len(lst) - 3), min(9, len(lst))):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result