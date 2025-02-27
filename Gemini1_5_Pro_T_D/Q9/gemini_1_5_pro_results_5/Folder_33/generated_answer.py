def all_odd_ints_inclusive(int_list):
    odd_ints = []
    for i in range(max(667, 0), min(775, len(int_list))):
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    return odd_ints