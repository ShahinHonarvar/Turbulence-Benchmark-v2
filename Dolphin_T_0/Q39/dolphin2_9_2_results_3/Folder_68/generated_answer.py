def return_n_greatest_chars(text):
    chars = list(text)
    chars.sort(key=lambda x: ord(x), reverse=True)
    return chars[:89]