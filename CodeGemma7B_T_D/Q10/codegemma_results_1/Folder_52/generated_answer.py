def all_odd_ints_exclusive(list1):
    result = []
    for item in list1[93:94]:
        if item % 2 != 0:
            result.append(item)
    return result