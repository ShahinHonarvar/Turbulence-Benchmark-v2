def filter_chars(s):
    chars_to_remove = [c for c in s[91:97] if 'j' < c < 'w']
    for char in set(chars_to_remove):
        s = s.replace(char, '')
    return s