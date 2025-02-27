def all_even_ints_inclusive(list):
    result = []
    for i in range(70, 85):
        if list[i] % 2 == 0:
            result.append(list[i])
    return result