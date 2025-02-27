def all_odd_ints_inclusive(lst):
    result = []
    for i in range(20, 201):
        if i < len(lst) and lst[i] % 2 != 0:
            result.append(lst[i])
    return result