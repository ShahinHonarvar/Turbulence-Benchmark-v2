def return_n_greatest_chars(s):
    chars = sorted([c for c in s if c.isalpha()], reverse=True)
    return sorted(chars[:58])