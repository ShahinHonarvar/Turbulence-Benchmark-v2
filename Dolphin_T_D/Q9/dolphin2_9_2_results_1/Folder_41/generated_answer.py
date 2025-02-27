def all_odd_ints_inclusive(lst):
    odd_list = []
    for i in range(6, 7):
        if lst[i] % 2 == 1:
            odd_list.append(lst[i])
    return odd_list