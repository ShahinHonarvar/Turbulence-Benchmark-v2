def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(max(32, 0), min(len(lst), 36)):
        if lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    return odd_ints