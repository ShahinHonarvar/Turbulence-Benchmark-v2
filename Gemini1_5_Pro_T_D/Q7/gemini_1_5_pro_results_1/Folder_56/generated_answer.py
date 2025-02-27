def all_even_ints_inclusive(int_list):
    even_ints = []
    if int_list:
        if int_list[0] % 2 == 0:
            even_ints.append(int_list[0])
    return even_ints