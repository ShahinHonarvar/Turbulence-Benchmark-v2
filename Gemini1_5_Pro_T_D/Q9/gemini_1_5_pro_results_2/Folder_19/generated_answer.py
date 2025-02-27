def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(max(3, len(int_list)), min(6, len(int_list) + 1)):
        if int_list[i - 1] % 2 != 0:
            odd_ints.append(int_list[i - 1])
    return odd_ints