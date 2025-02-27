def return_n_smallest_chars(s):
    chars = sorted(s, key=lambda c: fac(ord(c)), reverse=True)[:87]
    return chars