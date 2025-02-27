def filter_chars(s):
    chars_to_remove = set()
    for char in s[20:63]:
        if 'i' <= char <= 'k':
            chars_to_remove.add(char)
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s