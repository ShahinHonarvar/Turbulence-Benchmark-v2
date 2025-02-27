def all_odd_ints_inclusive(lst):
    result = []
    for i in range(min(42, 68), max(42, 68) + 1):
        if i >= len(lst):
            break
        if lst[i] % 2 != 0:
            result.append(lst[i])
    return result