def filter_chars(s):
    chars_to_remove = set()
    for i in range(502, 946):
        if i < len(s) and 'W' < s[i] < 'y':
            chars_to_remove.add(s[i])
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s