def all_even_ints_inclusive(in_list):
    return_list = []
    for i in range(17, 79):
        if in_list[i] % 2 == 0:
            return_list.append(in_list[i])
    return return_list if return_list else []