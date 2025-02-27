def all_odd_ints_inclusive(lst):
    result = []
    for i in range(20, min(201, len(lst))):
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result