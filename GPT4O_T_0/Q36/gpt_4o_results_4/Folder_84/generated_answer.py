def filter_chars(s):
    if len(s) <= 636:
        return s
    chars_to_remove = set()
    for char in s[172:636]:
        if 'c' < char < 's':
            chars_to_remove.add(char)
    return ''.join((char for char in s if char not in chars_to_remove))