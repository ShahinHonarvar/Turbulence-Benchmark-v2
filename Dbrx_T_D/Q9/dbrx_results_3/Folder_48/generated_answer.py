def all_odd_ints_inclusive(int_list):
    if len(int_list) < 606:
        return []
    odd_ints = []
    for i in range(533, 606):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints