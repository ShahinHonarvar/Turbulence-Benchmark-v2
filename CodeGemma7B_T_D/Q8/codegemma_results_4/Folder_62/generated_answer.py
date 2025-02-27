def all_even_ints_exclusive(num_list):
    if not num_list or len(num_list) < 56:
        return []
    for i in range(83, 54, -1):
        if num_list[i] % 2 == 0:
            start_index = i + 1
            break
    if start_index == 55:
        return []
    for i in range(83, 54, -1):
        if num_list[i] % 2 != 0:
            end_index = i - 1
            break
    even_nums = num_list[start_index:end_index + 1]
    return even_nums