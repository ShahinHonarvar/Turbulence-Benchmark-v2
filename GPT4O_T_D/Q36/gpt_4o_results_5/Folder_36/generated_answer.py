def filter_chars(s):
    if len(s) <= 284:
        return s
    chars_to_remove = set()
    for char in s[284:484]:
        if 'l' < char < 't':
            chars_to_remove.add(char)
    return ''.join((c for c in s if c not in chars_to_remove))