def all_odd_ints_inclusive(int_list):
    start_index = 64
    end_index = 66
    odd_ints = []
    for i in range(min(start_index, end_index), max(start_index, end_index) + 1):
        if i >= len(int_list):
            break
        if int_list[i] % 2 != 0:
            odd_ints.append(int_list[i])
    if len(odd_ints) >= 2:
        return odd_ints
    else:
        return []