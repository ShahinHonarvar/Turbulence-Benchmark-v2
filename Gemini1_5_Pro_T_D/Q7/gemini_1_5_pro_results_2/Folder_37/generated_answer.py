def all_even_ints_inclusive(int_list):
    even_ints = []
    for i in range(1, 6):
        if i % 2 == 0:
            try:
                even_ints.append(int_list[i])
            except:
                pass
    return even_ints