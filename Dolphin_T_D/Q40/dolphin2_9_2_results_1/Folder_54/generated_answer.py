def return_n_smallest_chars(s):
    chars = sorted(s, key=lambda c: ord(c))[:79]
    chars.sort(reverse=True)
    return chars