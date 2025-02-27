def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(max(0, min(74, len(lst))), min(96, len(lst))):
        if lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    return odd_ints