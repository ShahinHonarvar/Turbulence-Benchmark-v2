def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(87, 95):
        if i >= len(int_list) or i < 0:
            break
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints