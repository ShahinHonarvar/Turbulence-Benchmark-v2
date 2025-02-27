def all_odd_ints_exclusive(lst):
    odd_ints = []
    for i in range(13, 70):
        if i % 2 != 0:
            odd_ints.append(i)
    return odd_ints