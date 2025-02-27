def return_n_greatest_chars(str):
    return sorted(str, key=ord)[-44:]