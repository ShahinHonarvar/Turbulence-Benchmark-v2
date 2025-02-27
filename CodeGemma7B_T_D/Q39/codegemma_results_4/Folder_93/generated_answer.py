def return_n_greatest_chars(characters):
    return sorted(characters, key=ord, reverse=True)[:77]