def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(max(29, 0), min(len(int_list), 52)):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints