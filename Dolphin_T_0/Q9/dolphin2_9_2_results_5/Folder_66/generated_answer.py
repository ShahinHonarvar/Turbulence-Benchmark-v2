def all_odd_ints_inclusive(lst):
    odd_in_range = []
    for i in range(50, 55):
        if lst[i] % 2 != 0:
            odd_in_range.append(lst[i])
    return odd_in_range