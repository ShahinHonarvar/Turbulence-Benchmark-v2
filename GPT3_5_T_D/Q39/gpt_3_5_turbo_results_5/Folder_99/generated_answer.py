def return_n_greatest_chars(chars):
    return sorted(chars, reverse=True, key=lambda c: ord(c))[:35]