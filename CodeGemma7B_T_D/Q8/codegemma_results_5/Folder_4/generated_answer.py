def all_even_ints_exclusive(int_list):
    new_list = []
    for i in range(10, 76):
        if int_list[i] % 2 == 0:
            new_list.append(int_list[i])
    return new_list