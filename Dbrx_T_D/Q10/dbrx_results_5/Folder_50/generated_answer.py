def all_odd_ints_exclusive(int_list):
    if len(int_list) < 98:
        return []
    odd_ints = []
    for i in range(70, 98):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints