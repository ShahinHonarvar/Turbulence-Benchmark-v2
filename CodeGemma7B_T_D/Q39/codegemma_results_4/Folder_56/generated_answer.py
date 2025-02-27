def return_n_greatest_chars(unique_chars):
    unique_chars = list(set(unique_chars))
    unique_chars.sort(key=lambda x: ord(x))
    unique_chars.reverse()
    return unique_chars[:21]