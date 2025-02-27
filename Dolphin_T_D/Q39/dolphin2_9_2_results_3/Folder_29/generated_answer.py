def return_n_greatest_chars(s):
    chars_list = list(s)
    chars_sorted = sorted(chars_list, key=lambda c: -ord(c))
    return chars_sorted[:23]