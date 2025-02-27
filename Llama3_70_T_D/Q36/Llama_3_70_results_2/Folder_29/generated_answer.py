def filter_chars(s):
    chars_to_remove = set(s[46:68]).intersection(set((chr(i) for i in range(ord('H') + 1, ord('s')))))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s