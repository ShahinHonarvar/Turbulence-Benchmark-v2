def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(124, 855) if chr(i) >= '9' and chr(i) <= 's'))
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s