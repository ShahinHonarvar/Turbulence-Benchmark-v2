def all_odd_ints_exclusive(lst):
    odd_ints = []
    for i in range(1, len(lst) - 1):
        if lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    return odd_ints