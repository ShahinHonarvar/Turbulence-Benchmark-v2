def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(max(4, len(int_list) - 1)):
        if i > 3 and i < 5 and (int_list[i] % 2 == 0):
            even_ints.append(int_list[i])
    return even_ints