def all_even_ints_exclusive(list):
    result = []
    for i in range(len(list)):
        if i >= 0 and i <= 5 and (list[i] % 2 == 0):
            result.append(list[i])
    return result