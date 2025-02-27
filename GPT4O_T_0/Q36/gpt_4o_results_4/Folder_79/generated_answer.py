def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('!') + 1, ord('A'))))
    filtered_string = ''.join((c for i, c in enumerate(s) if c not in chars_to_remove or i <= 11 or i >= 46))
    return filtered_string