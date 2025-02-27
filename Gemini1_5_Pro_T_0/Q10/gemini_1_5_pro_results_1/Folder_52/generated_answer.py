def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(94, 95):
        if i >= len(int_list) or i < 0:
            continue
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints