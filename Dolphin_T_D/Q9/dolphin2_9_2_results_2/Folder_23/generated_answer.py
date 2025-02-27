def all_odd_ints_inclusive(lst):
    odd_lst = []
    for i in range(52, 72):
        if lst[i] % 2 != 0:
            odd_lst.append(lst[i])
    return odd_lst