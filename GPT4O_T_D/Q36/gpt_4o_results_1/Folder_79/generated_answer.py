def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('!') + 1, ord('A'))))
    filtered_chars = s[11:46][1:-1]
    for char in set(filtered_chars):
        if char in chars_to_remove:
            s = s.replace(char, '')
    return s