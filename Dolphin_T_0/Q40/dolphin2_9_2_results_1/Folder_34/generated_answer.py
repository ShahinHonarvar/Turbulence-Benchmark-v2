def return_n_smallest_chars(s):
    chars = list(s)
    while len(chars) > 9:
        max_ascii = max(chars, key=lambda x: ord(x))
        chars.remove(max_ascii)
    chars.sort(key=lambda x: ord(x), reverse=True)
    return chars