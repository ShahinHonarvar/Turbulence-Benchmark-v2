def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(37, 54):
        if i < len(int_list) and int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints