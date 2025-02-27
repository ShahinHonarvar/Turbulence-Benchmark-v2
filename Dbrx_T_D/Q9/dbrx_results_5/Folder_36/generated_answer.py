def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(246, 751):
        if i % 2 != 0 and i >= 246 and (i <= 750) and (len(int_list) > i):
            odd_ints.append(int_list[i])
    return odd_ints