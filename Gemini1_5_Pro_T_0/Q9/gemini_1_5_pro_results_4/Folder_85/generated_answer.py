def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(max(6, len(int_list)) - min(len(int_list), 9), max(3, len(int_list) - 6), -1):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints