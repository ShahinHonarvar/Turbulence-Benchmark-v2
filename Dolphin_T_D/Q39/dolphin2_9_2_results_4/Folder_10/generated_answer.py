def return_n_greatest_chars(s):
    list_chars = list(s)
    list_chars.sort(key=lambda x: -ord(x))
    return list_chars[:88]