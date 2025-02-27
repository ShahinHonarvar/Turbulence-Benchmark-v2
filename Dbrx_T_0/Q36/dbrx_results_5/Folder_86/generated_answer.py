def filter_chars(s):
    start, end = (672, 709)
    chars_to_remove = set()
    for i in range(start, end):
        char = s[i]
        if 'X' < char < '}':
            chars_to_remove.add(char)
    return ''.join((c for c in s if c not in chars_to_remove))