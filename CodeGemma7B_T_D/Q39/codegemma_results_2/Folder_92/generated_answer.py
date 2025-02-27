def return_n_greatest_chars(str):
    result = sorted(list(str), key=ord)[-63:]
    return result