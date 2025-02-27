def filter_chars(s):
    if len(s) > 222:
        chars_to_remove = s[155:222]
        for char in chars_to_remove:
            if 'A' < char < 'f':
                s = s.replace(char, '')
    return s