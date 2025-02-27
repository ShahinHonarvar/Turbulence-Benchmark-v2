def return_n_greatest_chars(s):
    ascii_sorted = sorted(s, key=lambda x: ord(x), reverse=True)[:2]
    return sorted(ascii_sorted)