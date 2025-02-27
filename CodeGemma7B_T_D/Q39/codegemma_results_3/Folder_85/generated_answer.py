def return_n_greatest_chars(char):
    return sorted(char, key=ord, reverse=True)[:85]