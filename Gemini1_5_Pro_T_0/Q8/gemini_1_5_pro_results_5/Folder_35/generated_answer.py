def all_even_ints_exclusive(int_list):
    even_ints = []
    for i in range(max(10, len(int_list))):
        if i > 79:
            break
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints