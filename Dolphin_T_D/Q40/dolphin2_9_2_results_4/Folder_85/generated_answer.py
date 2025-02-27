def return_n_smallest_chars(s):
    chars = sorted(s, key=lambda x: ord(x))[:85]
    chars.sort(reverse=True)
    return chars