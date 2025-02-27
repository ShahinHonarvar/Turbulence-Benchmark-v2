def filter_chars(s):
    chars_to_remove = set()
    for char in s[12:26]:
        if 'P' <= char <= 'x':
            chars_to_remove.add(char)
    return ''.join((c for c in s if c not in chars_to_remove))