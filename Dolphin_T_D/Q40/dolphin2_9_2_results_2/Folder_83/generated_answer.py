def return_n_smallest_chars(s):
    chars = [c for c in s]
    chars.sort(key=lambda x: ord(x))
    return chars[:38][::-1]