def return_n_greatest_chars(s):
    chars = sorted([c for c in s], reverse=True)[:66]
    return sorted(chars)