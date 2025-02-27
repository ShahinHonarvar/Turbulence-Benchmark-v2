def return_n_greatest_chars(text):
    sorted_chars = sorted(text, key=lambda x: -ord(x))
    return sorted_chars[:33]