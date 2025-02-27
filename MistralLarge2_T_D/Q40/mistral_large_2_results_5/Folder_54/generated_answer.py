def return_n_smallest_chars(s):
    return sorted([c for c in s if c.isprintable()], key=lambda x: ord(x))[:79][::-1]