def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(max(8, len(int_list)), 9):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints