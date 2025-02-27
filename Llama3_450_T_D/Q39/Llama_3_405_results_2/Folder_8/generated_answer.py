def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda c: ord(c), reverse=True)[:83]
    return sorted(sorted_chars)