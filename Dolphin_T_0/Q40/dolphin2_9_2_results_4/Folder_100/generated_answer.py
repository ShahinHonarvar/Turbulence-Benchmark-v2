def return_n_smallest_chars(s):
    chars = list(s)
    chars.sort(key=lambda c: ord(c))
    chars = chars[:72]
    chars.sort(reverse=True)
    return chars