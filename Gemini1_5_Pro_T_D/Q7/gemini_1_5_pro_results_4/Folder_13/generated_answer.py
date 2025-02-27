def all_even_ints_inclusive(int_list):
    even_ints = []
    for i in range(max(25, 0), min(len(int_list), 88)):
        if int_list[i] % 2 == 0:
            even_ints.append(int_list[i])
    return even_ints