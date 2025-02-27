def return_n_greatest_chars(str):
    if len(str) != len(set(str)):
        raise ValueError('Error')
    list = sorted(str, key=ord, reverse=True)
    return list[:29]