def return_n_greatest_chars(s):
    max_chars = [c for c in s if c.isalpha()]
    max_chars.sort(reverse=True)
    return max_chars[:63]