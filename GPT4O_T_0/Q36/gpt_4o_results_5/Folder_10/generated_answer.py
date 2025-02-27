def filter_chars(s):
    if len(s) <= 35:
        return s
    chars_to_remove = set((chr(i) for i in range(ord('!') + 1, ord('B'))))
    filtered_part = s[36:60]
    for char in filtered_part:
        if char in chars_to_remove:
            s = s.replace(char, '')
    return s