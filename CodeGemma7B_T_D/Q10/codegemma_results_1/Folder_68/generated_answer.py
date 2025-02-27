def all_odd_ints_exclusive(lst):
    odd_nums = []
    for i in range(9):
        if i % 2 != 0 and i != 8:
            odd_nums.append(lst[i])
    return odd_nums