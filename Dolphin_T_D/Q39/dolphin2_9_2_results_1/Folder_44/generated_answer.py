def return_n_greatest_chars(s):
    return sorted([ch for ch in s if ch.isascii()], key=lambda ch: -ord(ch))[:73]