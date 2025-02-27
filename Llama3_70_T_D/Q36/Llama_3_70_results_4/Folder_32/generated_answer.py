def filter_chars(s):
    s = list(s)
    chars_to_remove = set()
    for c in s[40:63]:
        if '7' < c < 'H':
            chars_to_remove.add(c)
    s = [c for c in s if c not in chars_to_remove]
    return ''.join(s)