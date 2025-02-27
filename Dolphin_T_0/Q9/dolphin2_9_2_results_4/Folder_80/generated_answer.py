def all_odd_ints_inclusive(lst):
    odd_nums = []
    for i in range(64, 67):
        if lst[i] % 2 != 0:
            odd_nums.append(lst[i])
    return odd_nums