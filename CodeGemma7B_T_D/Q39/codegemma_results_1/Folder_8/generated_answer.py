def return_n_greatest_chars(str):
    if len(str) > 83:
        str = str[:83]
    list = sorted(str, key=ord)
    return list[::-1]