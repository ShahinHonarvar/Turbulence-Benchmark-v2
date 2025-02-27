def return_n_greatest_chars(text):
    unique_chars = list(set(text))
    unique_chars.sort(key=ord, reverse=True)
    return unique_chars[:16]