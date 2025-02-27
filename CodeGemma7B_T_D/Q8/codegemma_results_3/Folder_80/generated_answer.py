def all_even_ints_exclusive(list):
    even_list = []
    for i in range(69, 97):
        if list[i] % 2 == 0:
            even_list.append(list[i])
    return even_list