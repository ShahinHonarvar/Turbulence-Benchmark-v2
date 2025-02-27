def return_n_greatest_chars(smth):
    list_chars = list(smth)
    list_chars.sort(reverse=True)
    return list_chars[:28]