def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(56, 99):
        if lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    if not odd_ints:
        return []
    return odd_ints