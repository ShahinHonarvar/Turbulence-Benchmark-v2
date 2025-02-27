def all_odd_ints_inclusive(lst):
    result = []
    for i in range(max(661, len(lst))):
        if i >= 924:
            break
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result