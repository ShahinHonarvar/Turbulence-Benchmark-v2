def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(max(4, len(int_list) - 1)):
        if i > 4 and i < len(int_list) - 1 and (int_list[i] % 2 != 0):
            odd_ints.append(int_list[i])
    return odd_ints