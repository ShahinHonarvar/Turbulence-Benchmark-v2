def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('A') + 1, ord('i'))))
    filtered_indices = s[28:75]
    for char in filtered_indices:
        if char in chars_to_remove:
            s = s.replace(char, '')
    return s