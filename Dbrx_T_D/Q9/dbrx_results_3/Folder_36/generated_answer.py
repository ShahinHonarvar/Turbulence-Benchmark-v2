def all_odd_ints_inclusive(some_list):
    odd_ints = []
    for i in range(len(some_list)):
        if i >= 246 and i <= 750:
            if some_list[i] % 2 != 0:
                odd_ints.append(some_list[i])
    return odd_ints