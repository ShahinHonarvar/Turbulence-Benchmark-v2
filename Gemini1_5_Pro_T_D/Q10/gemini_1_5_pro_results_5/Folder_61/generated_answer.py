def all_odd_ints_exclusive(int_lst):
    odd_ints = []
    for i in range(1, min(7, len(int_lst))):
        if int_lst[i] % 2 != 0:
            odd_ints.append(int_lst[i])
    return odd_ints