def all_odd_ints_exclusive(lst):
    odd_nums = []
    for i in range(20, 35):
        if lst[i] % 2 != 0:
            odd_nums.append(lst[i])
    return odd_nums if odd_nums else []