def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord, reverse=True)[:48]
    return sorted(sorted_chars, key=ord)