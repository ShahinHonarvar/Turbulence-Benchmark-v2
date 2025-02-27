def return_n_greatest_chars(string):
    list_chars = list(string)
    list_chars.sort(reverse=True)
    return list_chars[:44]