def all_even_ints_inclusive(int_list):
    even_ints = []
    for i in range(max(29, 0), min(len(int_list), 52)):
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints