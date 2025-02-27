def all_even_ints_exclusive(int_list):
    new_list = []
    for element in int_list:
        if element % 2 == 0 and element in range(15, 99):
            new_list.append(element)
    return new_list