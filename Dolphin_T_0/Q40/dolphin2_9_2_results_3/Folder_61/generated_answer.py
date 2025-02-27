def return_n_smallest_chars(s):
    chars = sorted([c for c in s], key=lambda c: ord(c))[:66]
    chars.sort(reverse=True)
    return chars