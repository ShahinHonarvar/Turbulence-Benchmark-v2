def return_n_greatest_chars(s):
    ascii_sorted = sorted(s, key=lambda c: ord(c))
    return sorted(ascii_sorted[-63:], key=lambda c: ord(c))