def all_even_ints_exclusive(int_list):
    even_range = []
    for i in range(73, 84):
        if int_list[i] % 2 == 0:
            even_range.append(int_list[i])
    return even_range