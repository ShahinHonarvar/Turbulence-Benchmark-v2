def all_odd_ints_exclusive(list_of_ints):
    if not list_of_ints:
        return []
    result = []
    for i in range(36, 85):
        if (i - 36) % 2 != 0 and i >= 36 and (i < 85):
            result.append(list_of_ints[i])
    return result