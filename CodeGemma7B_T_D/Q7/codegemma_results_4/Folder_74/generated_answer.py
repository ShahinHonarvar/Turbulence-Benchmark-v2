def all_even_ints_inclusive(int_list):
    evens = []
    for i in range(17, 79):
        if int_list[i] % 2 == 0:
            evens.append(int_list[i])
    return evens