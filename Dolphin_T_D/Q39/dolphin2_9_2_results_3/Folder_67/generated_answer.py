def return_n_greatest_chars(string):
    list_chars = list(string)
    list_chars.sort(key=lambda x: -ord(x))
    return list_chars[:66]