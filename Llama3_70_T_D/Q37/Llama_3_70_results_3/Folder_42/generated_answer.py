def filter_chars(s):
    chars_to_remove = set()
    for char in s[73:75]:
        if 'U' <= char <= 'l':
            chars_to_remove.add(char)
    return ''.join([c for c in s if c not in chars_to_remove])