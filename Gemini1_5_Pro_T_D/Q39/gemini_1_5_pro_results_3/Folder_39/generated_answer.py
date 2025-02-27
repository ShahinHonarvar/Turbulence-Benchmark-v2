def return_n_greatest_chars(text):
    return sorted(sorted(text, key=ord, reverse=True)[:23])