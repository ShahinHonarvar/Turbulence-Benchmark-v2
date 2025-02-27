def return_n_greatest_chars(string):
    list_of_chars = sorted(list(string), key=ord)
    return list_of_chars[-64:]