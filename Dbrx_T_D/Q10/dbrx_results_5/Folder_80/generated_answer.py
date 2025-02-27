def all_odd_ints_exclusive(int_list):
    if len(int_list) < 97:
        return []
    odd_ints = []
    for i in range(69, 97):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints