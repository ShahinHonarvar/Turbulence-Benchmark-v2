def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(max(246, len(int_list))):
        if i >= 246 and i <= 750 and (int_list[i] % 2 != 0):
            odd_ints.append(int_list[i])
    return odd_ints