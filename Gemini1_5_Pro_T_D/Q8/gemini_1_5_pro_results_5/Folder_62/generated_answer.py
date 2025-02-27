def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(55, 84):
        if i < len(int_list) and i >= 0:
            if int_list[i] % 2 == 0:
                even_ints.append(int_list[i])
    return even_ints