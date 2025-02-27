def return_n_greatest_chars(text):
    list_of_chars = sorted(list(text), key=ord)[-73:]
    list_of_chars.sort()
    return list_of_chars