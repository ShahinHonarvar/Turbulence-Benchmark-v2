def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(len(int_list)):
        if i >= 90 and i < 200 and (int_list[i] % 2 != 0):
            odd_ints.append(int_list[i])
    return odd_ints