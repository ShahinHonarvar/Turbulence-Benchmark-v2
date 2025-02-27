def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('!') + 1, ord('A'))))
    filtered_string = ''.join((c for c in s if c not in chars_to_remove or not 11 < s.index(c) < 46))
    return filtered_string