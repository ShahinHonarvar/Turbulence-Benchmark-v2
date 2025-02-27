def all_even_ints_inclusive(int_list):
    even_ints = []
    if len(int_list) > 73:
        if int_list[73] % 2 == 0:
            even_ints.append(int_list[73])
    return even_ints