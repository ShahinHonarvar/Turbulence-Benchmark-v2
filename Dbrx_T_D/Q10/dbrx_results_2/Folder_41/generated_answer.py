def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(8, 10):
        if len(int_list) > i and int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints