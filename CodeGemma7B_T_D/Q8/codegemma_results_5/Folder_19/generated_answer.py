def all_even_ints_exclusive(int_list):
    evens = []
    for i in range(2, 5):
        if int_list[i] % 2 == 0:
            evens.append(int_list[i])
    return evens