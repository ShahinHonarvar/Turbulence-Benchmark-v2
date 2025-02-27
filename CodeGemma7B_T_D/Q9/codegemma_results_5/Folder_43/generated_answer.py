def all_odd_ints_inclusive(lst):
    odd_nums = []
    for i in range(68, 87):
        if lst[i] % 2 == 1:
            odd_nums.append(lst[i])
    return odd_nums