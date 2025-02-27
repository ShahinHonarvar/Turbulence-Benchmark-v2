def all_odd_ints_inclusive(int_list):
    odd_ints = []
    if len(int_list) > 10:
        for i in range(10, 11):
            if int_list[i] % 2 != 0:
                odd_ints.append(int_list[i])
    return odd_ints