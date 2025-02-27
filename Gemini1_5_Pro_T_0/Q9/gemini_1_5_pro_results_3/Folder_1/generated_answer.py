def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(max(31, len(int_list))):
        if i >= len(int_list):
            break
        if i >= 31 and i <= 72 and (int_list[i] % 2 != 0):
            odd_ints.append(int_list[i])
    return odd_ints