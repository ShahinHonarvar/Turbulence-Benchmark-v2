def all_odd_ints_exclusive(lst):
    odd_list = []
    for i in range(1, len(lst) - 1):
        if lst[i] % 2 != 0:
            odd_list.append(lst[i])
    return odd_list