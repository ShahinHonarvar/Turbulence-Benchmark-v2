def all_odd_ints_exclusive(int_list):
    odd_ints = []
    if len(int_list) >= 90:
        for i in range(86, 90):
            if int_list[i] % 2 != 0:
                odd_ints.append(int_list[i])
    return odd_ints