def all_even_ints_inclusive(lst):
    result = []
    for i in range(max(0, min(62, len(lst))), min(93, len(lst))):
        if lst[i] % 2 == 0:
            result.append(lst[i])
    return result