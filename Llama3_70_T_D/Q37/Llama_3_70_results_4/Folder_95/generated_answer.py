def filter_chars(s):
    chars_to_filter = set()
    for char in s[35:41]:
        if ')' <= char <= 'l':
            chars_to_filter.add(char)
    return ''.join((c for c in s if c not in chars_to_filter))