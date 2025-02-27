def all_even_ints_inclusive(num_list):
    temp_list = []
    for i in range(12, 93):
        if num_list[i] % 2 == 0:
            temp_list.append(num_list[i])
    if len(temp_list) == 0:
        return []
    return temp_list