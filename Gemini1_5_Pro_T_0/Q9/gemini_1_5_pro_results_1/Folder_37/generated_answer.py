def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(1, 6):
        if i <= len(int_list) and int_list[i - 1] % 2 != 0:
            odd_ints.append(int_list[i - 1])
    return odd_ints