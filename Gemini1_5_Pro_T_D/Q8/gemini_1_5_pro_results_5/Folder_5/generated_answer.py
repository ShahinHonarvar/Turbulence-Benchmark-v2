def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(max(2, len(int_list) - 3)):
        if int_list[i + 2] % 2 == 0:
            even_ints.append(int_list[i + 2])
    return even_ints