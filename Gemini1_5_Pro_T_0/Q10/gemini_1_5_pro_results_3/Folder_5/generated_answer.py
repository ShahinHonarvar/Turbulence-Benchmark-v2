def all_odd_ints_exclusive(lst):
    result = []
    for i in range(3, 7):
        if i < len(lst) and lst[i] % 2 != 0:
            result.append(lst[i])
    return result