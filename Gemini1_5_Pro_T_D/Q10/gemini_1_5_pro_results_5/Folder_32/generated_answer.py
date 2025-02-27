def all_odd_ints_exclusive(int_list):
    odd_ints = []
    for i in range(12, 76):
        if i not in range(len(int_list)):
            return odd_ints
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints