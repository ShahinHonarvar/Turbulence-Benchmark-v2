def return_n_smallest_chars(s):
    return sorted([c for c in s if c.isalpha()], key=lambda x: ord(x), reverse=True)[:27]