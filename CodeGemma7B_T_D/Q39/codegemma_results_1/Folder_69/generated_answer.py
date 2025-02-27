def return_n_greatest_chars(text):
    return sorted(text, key=lambda ch: ord(ch), reverse=True)[:65]