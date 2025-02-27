def all_even_ints_inclusive(lst):
    result = []
    try:
        for i in range(73, 74):
            if lst[i] % 2 == 0:
                result.append(lst[i])
    except IndexError:
        pass
    return result