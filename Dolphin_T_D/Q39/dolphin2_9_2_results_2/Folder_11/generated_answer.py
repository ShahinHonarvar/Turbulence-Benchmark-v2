def return_n_greatest_chars(s):
    max_chars = sorted([c for c in s if c.isalpha()], reverse=True)[:17]
    return sorted(max_chars)