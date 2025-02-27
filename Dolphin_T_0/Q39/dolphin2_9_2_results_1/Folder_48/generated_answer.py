def return_n_greatest_chars(s):
    return sorted([c for c in s if c.isalpha()], reverse=True)[:12]