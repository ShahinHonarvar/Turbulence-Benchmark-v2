def filter_chars(s):
    if len(s) <= 57:
        return s
    chars_to_remove = set()
    for char in s[58:69]:
        if '(' < char < 'W':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))