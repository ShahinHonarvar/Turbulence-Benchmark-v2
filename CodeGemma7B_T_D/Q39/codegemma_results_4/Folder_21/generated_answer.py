def return_n_greatest_chars(string):
    list_of_chars = sorted(string, key=ord, reverse=True)
    return list_of_chars[:44]