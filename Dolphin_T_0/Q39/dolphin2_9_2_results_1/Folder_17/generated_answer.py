def return_n_greatest_chars(chars):
    return sorted(chars, key=lambda c: ord(c), reverse=True)[:11]