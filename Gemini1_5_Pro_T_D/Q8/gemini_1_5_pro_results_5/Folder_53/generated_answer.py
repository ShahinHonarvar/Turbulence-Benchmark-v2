def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(max(101, len(int_list))):
        if i >= 100 and i < 101 and (int_list[i] % 2 == 0):
            even_ints.append(int_list[i])
    return even_ints