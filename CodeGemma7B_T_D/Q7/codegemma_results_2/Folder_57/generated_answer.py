def all_even_ints_inclusive(list):
    if not list:
        return []
    result = []
    for i in range(27, 56):
        if list[i] % 2 == 0:
            result.append(list[i])
    return result