def all_odd_ints_inclusive(num_list):
    odd_int_list = []
    for i in range(56, 99):
        if num_list[i] % 2 != 0:
            odd_int_list.append(num_list[i])
    if not odd_int_list:
        return []
    return odd_int_list