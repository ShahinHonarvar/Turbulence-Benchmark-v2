def return_n_greatest_chars(str):
    list_chars = list(str)
    list_chars.sort(key=ord)
    return list_chars[-23:]