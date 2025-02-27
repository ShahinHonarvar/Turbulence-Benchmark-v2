def return_n_smallest_chars(string):
    lst_of_chars = sorted([x for x in string], key=ord)
    return lst_of_chars[:52]