def return_nth_smallest_ascii(str):
    alphabet_list = []
    for c in str[12:88]:
        alphabet_list.append(c)
    alphabet_list.sort()
    return alphabet_list[16]