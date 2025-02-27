def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(56, 83):
        if i > len(int_list) - 1:
            break
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints