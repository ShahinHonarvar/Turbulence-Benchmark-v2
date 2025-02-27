def all_even_ints_exclusive(list):
    even_list = []
    for i in list:
        if i % 2 == 0 and 29 < i < 53:
            even_list.append(i)
    if even_list == []:
        return []
    return even_list