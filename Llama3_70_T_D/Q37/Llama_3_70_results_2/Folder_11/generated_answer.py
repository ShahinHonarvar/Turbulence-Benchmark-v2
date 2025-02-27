def filter_chars(s):
    chars_to_remove = [chr(i) for i in range(29, 98) if '-' <= chr(i) <= 'n']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s