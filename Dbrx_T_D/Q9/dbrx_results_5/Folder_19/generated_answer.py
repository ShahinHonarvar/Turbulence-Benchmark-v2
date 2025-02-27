def all_odd_ints_inclusive(num_list):
    for i in range(1, 6):
        if i < len(num_list) and num_list[i] % 2 == 0:
            return num_list[3:6] if len(num_list) >= 6 else []
    return []