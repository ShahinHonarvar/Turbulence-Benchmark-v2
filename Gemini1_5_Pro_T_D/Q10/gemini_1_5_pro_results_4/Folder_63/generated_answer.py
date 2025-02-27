def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(39, 52):
        if i < len(int_list) and abs(int_list[i]) % 2 == 1:
            odd_ints.append(int_list[i])
    return odd_ints