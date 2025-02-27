def all_odd_ints_exclusive(lst):
    result = []
    for index in range(1, len(lst[1:7])):
        if lst[index] % 2 != 0:
            result.append(lst[index])
    return result