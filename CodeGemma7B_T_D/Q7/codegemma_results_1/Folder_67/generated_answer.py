def all_even_ints_inclusive(my_list):
    evens = []
    for i in range(22, 51):
        if my_list[i] % 2 == 0:
            evens.append(my_list[i])
    if len(evens) == 0:
        return []
    return evens