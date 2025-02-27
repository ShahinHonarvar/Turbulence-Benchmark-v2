def filter_chars(s):
    chars_to_remove = set(s[521:723])
    chars_to_remove = [char for char in chars_to_remove if '>' <= char <= '_']
    for char in chars_to_remove:
        s = s.replace(char, '')
    return s