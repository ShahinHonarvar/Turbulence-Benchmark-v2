def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(51, 92):
        if i % 2 != 0 and i < len(int_list):
            odd_ints.append(int_list[i])
    return odd_ints