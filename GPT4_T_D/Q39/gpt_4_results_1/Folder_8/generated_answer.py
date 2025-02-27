def return_n_greatest_chars(string):
    greatest_chars = sorted(list(string), key=ord)[-83:]
    sorted_chars = sorted(greatest_chars)
    return sorted_chars