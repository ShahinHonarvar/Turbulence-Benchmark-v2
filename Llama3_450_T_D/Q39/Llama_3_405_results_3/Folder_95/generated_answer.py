def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda c: ord(c), reverse=True)[:36]
    return sorted(sorted_chars)