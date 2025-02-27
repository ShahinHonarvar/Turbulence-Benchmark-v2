def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(max(30, len(int_list))):
        if i > 30 and i < 200 and (int_list[i] % 2 == 0):
            even_ints.append(int_list[i])
    return even_ints