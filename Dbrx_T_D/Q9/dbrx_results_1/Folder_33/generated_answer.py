def all_odd_ints_inclusive(lst):
    odd_ints = []
    for i in range(667, 775):
        if i >= 0 and lst[i] % 2 != 0:
            odd_ints.append(lst[i])
    return odd_ints