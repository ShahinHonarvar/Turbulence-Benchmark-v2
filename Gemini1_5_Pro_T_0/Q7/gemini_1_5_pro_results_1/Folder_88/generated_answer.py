def all_even_ints_inclusive(int_list):
    even_ints = []
    for i in range(4, 9):
        if i < len(int_list) and int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints